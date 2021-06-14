Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #importing library
>>> from tkinter import *
>>> from tkinter import ttk
>>> window =Tk()
>>> #Declaring Window Title
>>> window.title('Registration Screen')
''
>>> window.geometry('300x300')
''
>>> window.configure(background ='green');
>>> firstname =Label(window,text ='firstname').grid(row=0,column=0)
>>> lastname =Label(window,text ='lastname').grid(row=1,column=0)
>>> email =Label(window,text ='Email Id').grid(row=2,column=0)
>>> Mobile =Label(window,text ='Contact number').grid(row=3,column=0)
>>> firstname1 =Entry(window).grid(row=0,column=1)
>>> lastname1 =Entry(window).grid(row=1,column=1)
>>> Email =Entry(window).grid(row=2,column=1)
>>> Mobile =Entry(window).grid(row=3,column=1)
>>> #fubction declaration
>>> def clicked():
	res = 'Welcome to' + txt.get()

	
>>> lbl.comnfigure(text=res)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lbl.comnfigure(text=res)
NameError: name 'lbl' is not defined
>>> def clicked():
	res = 'Welcome to' + txt.get()
lbl.configure(text=res)
SyntaxError: invalid syntax
>>> btn=ttk.Button(window,text='Submit').grid(row=4,column=0)
>>> window.mainloop()
