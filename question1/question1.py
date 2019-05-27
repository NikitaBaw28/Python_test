def add():
	a=100
	b=200
	print(a+b)


#print(a)	##here it shows error as a has only been defined in the function,
#print(b)	## it is a local variable only to the function


def sub():
	global x,y
	a=x=300
	b=y=400
	print(y-x)


print(a)
print(b)
