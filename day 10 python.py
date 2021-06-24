Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #banking concept
>>> class account:
	def __init__(self,name,adress):
		self.name = name
		self.adress = adress
	def printname(self):
		print(self.name,self.adress)

		
>>> class bank(account):
	def __init__(name,adress)
	
SyntaxError: invalid syntax
>>> class bank(account):
	def __init__(self,name,adress,acnumber):
		super().__init__(name,adress)
		self.number = acnumber
	def welcome(self):
		print("welcome",self.name,"to your account number",self.number)

		
>>> a = bank("kiran","TN",1234)
>>> a.welcome()
welcome kiran to your account number 1234
>>> #E-commerce concept
>>> class account:
	def __init__(self,name,adress):
		self.name = name
		self.adress = adress
	def printname(self):
		print(self.name,self.adress)

		
>>> class flipcart(account):
	def __init__(self,name,adress,acnumber):
		super().__init__(name,adress)
		self.number = acnumber
	def welcome(self):
		print("welcome",self.name,"to your order id id ",self.number)

		
>>> a=flipcart("raj","chennai","ID543")
>>> a.welcome()
welcome raj to your order id id  ID543
>>> 