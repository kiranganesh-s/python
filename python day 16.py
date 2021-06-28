Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #multiplication using lambda function
>>> a= lambda x,y:x*y
>>> print(a(2,3))
6
>>> #2
>>> from functools import reduce
>>> fib = lambda n: reduce(lambda x , _:x+[x[-1]+x[-2]],range(n-2),[0,1])
>>> print(fib(5))
[0, 1, 1, 2, 3]
>>> #3
>>> nums =[1,4,3,5,6]
>>> n=2
>>> filtered_numbers = list(map(lambda number : number*n,nums))
>>> print(flittered_numbers)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(flittered_numbers)
NameError: name 'flittered_numbers' is not defined
>>> print(filtered_numbers)
[2, 8, 6, 10, 12]
>>> #4
>>> list1 =[12,8,10,9,53]
>>> m=9
>>> divisible_numbers=list(filter(lambda number:(number%m==0),list1))
>>> print(divisible_numbers)
[9]
>>> #5
>>> list2=[1,2,3,4,5,6,7,8]
>>> even_numbers=list(filter(lambda number:(number%2==0),list2))
>>> print(even_numbers)
[2, 4, 6, 8]
>>> 