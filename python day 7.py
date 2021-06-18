Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def function(a,b):
	print('Addition of a,b is:',a+b)
	print('Subtraction of a,b is:',a-b)
	print('Multiplication of a,b is:',a*b)
	print('Division of a,b is:',a/b)

	
>>> a=int(input('Enter first number:'))
Enter first number:5
>>> b=int(input('Enter second number:'))
Enter second number:7
>>> function(a,b)
Addition of a,b is: 12
Subtraction of a,b is: -2
Multiplication of a,b is: 35
Division of a,b is: 0.7142857142857143
>>> 
>>> def covid(name,temperature=98):
	print('patient name is:',name)
	print('body temperature is:',temperature)

	
>>> covid('rajesh')
patient name is: rajesh
body temperature is: 98
>>> 