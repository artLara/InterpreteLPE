import re
import os
import os.path

def deleteTabs(cad):
	tabs = re.findall("\t", cad)
	return cad[len(tabs)::].rstrip()

def variableFormat(cad):
	cad = deleteTabs(cad)

	newCad = ''
	i = 0
	while i < len(cad):
		if ' ' != cad[i]:
			newCad += cad[i]
			
		i += 1

	return newCad

def analyzer(path='mult.txt', external=False, verbose = False):
	name = path.split('.')[0]
	variables = set()
	functions_names = set()
	constants = set()
	identation = 0
	body = 'x1 = 0\n'
	body += 'x2 = 0\n'
	body += 'x3 = 0\n'
	body += 'z1 = 0\n'
	body += 'z2 = 0\n'
	body += 'z3 = 0\n'
	globals_names = ['global x1', 'global x2', 'global x3', 'global z1', 'global z2', 'global z3']
	error = False
	try:
		with open(path) as f:
			f = list(f)
			for index, line in enumerate(f):
				if line.find(':') != -1: #For functions
					aux = line.rstrip().split(':')[0]
					if aux != name:
						aux += '_'+name
					functions_names.add(aux)

			for index, line in enumerate(f):
				# print(line)
				if line.find('end') != -1:
					continue
				elif line.find(':') != -1: #For functions
					aux = line.rstrip().split(':')[0]
					if aux != name:
						aux += '_'+name

					body += 'def ' + aux + '():\n'
					for g in globals_names:
						body += '\t' + g + '\n'

				elif line.find('<') != -1: #Asignacion de variables
					aux = line.rstrip().split('<')
					varDest = aux[0]
					varOrig = aux[1][1:len(aux[1])-1]
					body += varDest + ' = ' + varOrig + '\n'

					varDest = variableFormat(varDest)
					if varDest.isnumeric():
						constants.add(varDest)
					else:
						variables.add(variableFormat(varDest))
					
					varOrig = variableFormat(varOrig)
					if varOrig.isnumeric():
						constants.add(varOrig)
					else:
						variables.add(variableFormat(varOrig))

				elif line.find('incr') != -1: #Incremento
					tabs = re.findall("\t", line)
					aux = line.rstrip().split()[1]
					aux = aux[:len(aux)-1]
					for i in tabs:
						aux = i + aux
					body += aux + ' += 1\n'

					aux = variableFormat(aux)
					if aux.isnumeric():
						print('Error: incremento a una contante en la línea', index+1)
						error = True
						break
					else:
						variables.add(variableFormat(aux))

				elif line.find('decr') != -1: #Decremento
					tabs = re.findall("\t", line)
					aux = line.rstrip().split()[1]
					aux = aux[:len(aux)-1]
					# print('tabs=',tabs)
					for i in tabs:
						aux = i + aux
					body += aux + ' -= 1\n'

					aux = variableFormat(aux)
					if aux.isnumeric():
						print('Error: decremento a una contante en la línea', index+1)
						error = True
						break
					else:
						variables.add(variableFormat(aux))

				elif line.find('clear') != -1: #Clear
					tabs = re.findall("\t", line)
					aux = line.rstrip().split()[1]
					aux = aux[:len(aux)-1]
					# print('tabs=',tabs)
					for i in tabs:
						aux = i + aux
					body += aux + ' = 0\n'

					aux = variableFormat(aux)
					if aux.isnumeric():
						print('Error: clear a una contante en la línea', index+1)
						error = True
						break
					else:
						variables.add(variableFormat(aux))

				elif line.find('while') != -1: #While
					tabs = re.findall("\t", line)
					aux = line.rstrip().split()[1]
					aux = "while " + aux + " != 0:"
					for i in tabs:
						aux = i + aux
					body += aux + '\n'
				else:
					aux = deleteTabs(line)
					if aux in functions_names or aux + '_'+name in functions_names:
						tabs = re.findall("\t", line)
						if aux != name:
							aux += '_'+name
						for i in tabs:
							aux = i + aux

						body += aux + '()\n'

					elif isExternalFunction(aux):
						functions_names.add(aux)
						ext = analyzer(aux+'.txt', external=True)
						if ext == None:
							print('Error en la funcion externa'+aux)

						body = ext + body
						tabs = re.findall("\t", line)
						for i in tabs:
							aux = i + aux

						body += aux + '()\n'

					elif aux in variables:
						print('Syntax Error: variable', aux, 'mal usada')

					elif aux in constants:
						print('Syntax Error: constante', aux, 'mal usada')
					else:
						if aux == '':
							continue
						print('"{}" no definida en la línea {}'.format(aux, index+1))
						error = True
						break

		if not error:
			if not external:
				body += 'print(z1)\n'
			if verbose:
				print('Funciones encontradas:', functions_names)
				print('Variables encontradas:', variables)
				print('Constantes encontradas:', constants)

				print('Programa python:')
				print(body)
			return body

		return None
	except FileNotFoundError:
		print('Archivo no encontrado, verifiquelo por favor')
		return None


	# break

def isExternalFunction(filename):
	return os.path.exists(filename+'.txt')
def writeProgramm(nameFile, body):
	text_file = open(nameFile+'.py', "w")
	text_file.write(body)
	text_file.close()

def run(name):
	command = "python " + name + ".py"
	output = os.popen(command).read()
	print('\n\tSalida del programa python:', output)

# analyzer(verbose=True)
