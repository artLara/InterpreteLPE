x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x1
def H_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x3
	z1 += 1
def suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_suma()
	aux = x2
	x2 = 0
	while aux != 0:
		x3  =  z1
		H_suma()
		x2 += 1
		aux -= 1
x1  =  3
x2  =  2
suma()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_pred():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = 0
def H_pred():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	x1 += 1
def pred():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_pred()
	aux = x1
	x1 = 0
	while aux != 0:
		z1  =  x1
		H_pred()
		aux -= 1
x1  =  0
pred()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_monus():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1  =  x1
def H_monus():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	pred()
def monus():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_monus()
	aux  =  x2
	x2 = 0
	aux1  =  x1
	while aux != 0:
		x1  =  z1
		H_monus()
		x1  =  aux1
		x2 += 1
		aux -= 1
x1  =  3
x2  =  2
monus()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def eq():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = 0
	ox1  =  x1
	ox2  =  x2
	monus()
	res1  =  z1
	x1  =  x2
	x2  =  ox1
	monus()
	res2  =  z1
	x1  =  res1
	x2  =  res2
	suma()
	res3  =  z1
	uno = 0
	uno += 1
	x1  =  uno
	x2  =  res3
	monus()
	x1  =  ox1
	x2  =  ox2
x1  =  7
x2  =  7
eq()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x1
def H_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x3
	z1 += 1
def suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_suma()
	aux = x2
	x2 = 0
	while aux != 0:
		x3  =  z1
		H_suma()
		x2 += 1
		aux -= 1
x1  =  3
x2  =  2
suma()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x1
def H_suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = x3
	z1 += 1
def suma():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_suma()
	aux = x2
	x2 = 0
	while aux != 0:
		x3  =  z1
		H_suma()
		x2 += 1
		aux -= 1
x1  =  3
x2  =  2
suma()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_mult():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = 0
def H_mult():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	suma()
def mult():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_mult()
	aux = x2
	x2 = 0
	while aux != 0:
		aux2  =  x2
		x2  =  z1
		H_mult()
		x2  =  aux2
		x2 += 1
		aux -= 1
x1  =  9
x2  =  9
mult()
x1 = 0
x2 = 0
x3 = 0
z1 = 0
z2 = 0
z3 = 0
def G_coc():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	z1 = 0
def coc():
	global x1
	global x2
	global x3
	global z1
	global z2
	global z3
	G_coc()
	ox1  =  x1
	ox2  =  x2
	aux  =  x1
	auxC = 0
	countX = 0
	while aux != 0:
		x2  =  ox2
		x1  =  auxC
		mult()
		x1  =  z1
		suma()
		x2  =  z1
		x1  =  countX
		x1 += 1
		eq()
		x2  =  z1
		x1  =  auxC
		suma()
		x1  =  ox1
		x2  =  ox2
		auxC  =  z1
		countX += 1
		aux -= 1
x1  =  0
x2  =  1
coc()
print(z1)
