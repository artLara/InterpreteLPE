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
print(z1)
