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
x2  =  3
monus()
print(z1)
