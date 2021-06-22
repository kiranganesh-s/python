Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  #1
>>> list1 = [1,2,3]
>>> add =2
>>> for i in list1:
	print(i+add)
	i+=1

	
3
4
5
>>> #2 pattern
>>> n=int(input("enter the number of rows:"))
enter the number of rows:5
>>> for i in range(n):
	for j in range(n-i-1,-1,-1):
		print(j+1,end=" ")

		
5 4 3 2 1 4 3 2 1 3 2 1 2 1 1 
>>> print()

>>> #3 fibonacci series
>>> def fib(n):
	a = 0
	b = 1
	if n==1:
		print(a)
	else:
		print(a)
		print(b)
		for i in range(2,n):
			c= a+b
			a=b
			b=c
			print(c)

			
>>> n = int(input("enter a number"))
enter a number10
>>> fib(n)
0
1
1
2
3
5
8
13
21
34
SyntaxError: invalid syntax
>>> #5
>>> n=9
>>> for i in range (1,11):
	print(n,"x",i,"=",n*i)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> #4
>>> print("amstrong number: finding length of number and total sum of power of each difitis number equal to number then called amstrong number")
amstrong number: finding length of number and total sum of power of each difitis number equal to number then called amstrong number
>>> i = int(input("enter a number"))
enter a number7
>>> num=i
>>> total=0
>>> n=len(str(i))
>>> while(i!=0)
SyntaxError: invalid syntax
>>> while(i!=0):
	digit=i%10
	total=total+digit**n
	i=i//10

	
>>> if num==total:
	print("amstrong number")
else:
	print("non amstrong number")

	
amstrong number
>>> #6
>>> n=int(input("enter a number"))
enter a number7
>>> if n>0:
	print("positive number")
elif m==0
SyntaxError: invalid syntax
>>> elif m==0:
	
SyntaxError: invalid syntax
>>> if n>0:
	print("positive number")
elif m==0:
	print("number equal to zero")
else:
	print("negative number")

	
positive number
>>> #7
>>> d=int(input("enter the number of days :"))
enter the number of days :7
>>> y=int(d/365)
>>> print(y,"year")
0 year
>>> #8
>>> import math
>>> x=90
>>> print
<built-in function print>
>>> print(math.sin(x))
0.8939966636005579
>>> print(math.cos(x))
-0.4480736161291701
>>> print(math.tan(x))
-1.995200412208242
SyntaxError: invalid syntax
>>> #9
>>> num1=int(input("enter a number"))
enter a number7
>>> operator = input("+,-,*,/")
+,-,*,/
>>> num2=int(input("enter a number"))
enter a number5
>>> out=0
>>> if operator =="+":
	out=num1+num2
if operator =="=":
	
SyntaxError: invalid syntax
>>> if operator =="+":
	out=num1+num2

	
>>>  if operator =="-":
	out=num1-num2
	
SyntaxError: unexpected indent
>>> if operator =="-":
	out=num1-num2

	
>>> if operator =="*":
	out=num1*num2

	
>>> if operator =="/":
	out=num1/num2

	
>>> print("answer is: ",out)
answer is:  0
>>> 