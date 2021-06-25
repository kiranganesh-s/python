Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file1=open("30days30houroperations.txt","w+")
>>> file1.write("I have  completed 10 days successfully \n")
40
>>> file1.close()
>>> file1=open("30days30houroperations.txt","r+")
>>> print(file1.read())
I have  completed 10 days successfully 

>>> #2
>>> file1=open("30days30houroperations.txt","a+")
>>> file1.write("Kiran Ganesh \n")
14
>>> file1.close()
>>> file1=open("30days30houroperations.txt","r+")
>>> print(file1.read())
I have  completed 10 days successfully 
Kiran Ganesh 

>>> 