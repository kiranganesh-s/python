Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hours="thirty"
>>> print(hours)
thirty
>>> days="thirty days"
>>> print(days[0])
t
>>> challenge="i will win"
>>> print(challenge[7:10])
win
>>> challenge="i will win"
>>> print(len(challenge))
10
>>> challenge="i will win"
>>> print(challenge.lower())
i will win
>>> challenge="i will win"
>>> print(challenge.upper())
I WILL WIN
>>> a="30 days"
>>> b="30 hours"
>>> c=a
>>> c=a
>>> c=a+b
>>> print(c)
30 days30 hours
>>> a="30 days"
>>> b="30 hours"
>>> c=a+" "+b
>>> print(c)
30 days 30 hours
>>> text="thirty days and thirty hours"
>>> x=test.casefold()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x=test.casefold()
NameError: name 'test' is not defined
>>> text="thirty days and thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> text="thirty days and thirty hours"
>>> x=text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> text="thirty days and thirty hours"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> text="thirty days and thirty hours"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> text="thirty days and thirty hours"
>>> x=text.find(i)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x=text.find(i)
NameError: name 'i' is not defined
>>> text="thirty days and thirty hours"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> text="thirty days"
>>> x=text.isalpha()
>>> print(x)
False
>>> text="thirty days"
>>> x=text.isalnum()
>>> print(x)
False
>>> 