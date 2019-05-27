class A:		##we create classes
	def __init__(self):
		self.name="Nikita"
		self.id="007"
	def func(self):
		print("--In class A--")
		ip=input("Enter a string")
		print(ip)
		print(self.name)
		print(self.id)

class B(A):  ##here class B inherits from class A
	def func(self):
		print("--In class B--")
		self.like="I like apples"
		ip2=input("Enter a fruit ")
		print(self.like+" and "+ip2)
		self.w="class B"
		self.w1="varia" 

class c(B,A):
	def func2(self): 	#here class C inherits from class A and B, also called multiple inheritance
		B.func(self)
		print("--In class C--")
		print(self.name)
		print(self.id)
		print(self.w)
		print(self.w1)
		print(self.like)



c1=A() ##we create objects for the classes
c2=B()
c3=c()

c1.func() ## calling the functions in classes	
c2.func()
c3.func2()

