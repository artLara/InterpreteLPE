from interprete import analyzer
from interprete import run
from interprete import writeProgramm


while True:
	# print('Introduzca la ruta absoluta del MP a convertir 0 para salir:')
	path = input('\nIntroduzca la ruta absoluta del MP a convertir 0 para salir:')
	if path == '0':
		print('Vuelva pronto :)')
		break

	else:
		verbose = input('\nOprima 1 para imprimir el programa python junto con sus datos o 0 para solo interpretar:')
		if verbose == '0':
			res = analyzer(path)
		else:
			res = analyzer(path, verbose=True)

		if res != None:

			name = path.split('.')[0]
			writeProgramm(name, res)
			# print('Name=', name)
			run(name)
