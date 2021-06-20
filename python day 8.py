Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={"a":1,"b":2}
>>> dict2={"c":3,"d":4}
>>> dict3=(dict2.update(dict1))
>>> print(dict2)
{'c': 3, 'd': 4, 'a': 1, 'b': 2}
>>> #sorting and convert list into set
>>> list1 = [4,3,2,1]
>>> list2 =list1[::-1]
>>> set1 = set(list2)
>>> print(set1)
{1, 2, 3, 4}
>>> #program to list numbers of item in a dictionarykey
>>> names ={3:"a",2:"b",1:"c"}
>>> list3 =dict.keys(names)
>>> print("list of dictionary keys",list3)
list of dictionary keys dict_keys([3, 2, 1])
>>> sorted_list3 = sorted(list3)
>>> print("sorting the list of dictionary keys",sorted_list3)
sorting the list of dictionary keys [1, 2, 3]
>>> #sorting list without using function
>>> names={3:"a",,2:"b",1:"c"}
SyntaxError: invalid syntax
>>> names={3:"a",2:"b",1:"a"}
>>> list4 = dict.keys(names)
>>> list3 = list(list4)
>>> print(list3)
[3, 2, 1]
>>> 
>>> asscending_list = list3[::-1]
>>> print(asscending_list)
[1, 2, 3]
>>> #4
>>> string1 = input("enter a string")
enter a string kiran
>>> string = string1[0:10]
>>> print(string)
 kiran
>>> firstword = string[0:3]
>>> print(firstword)
 ki
>>> user_word = input("enter a word")
enter a word arav
>>> final_string = string.replace(firstword,user_word)
>>> print(final_string)
 aravran
>>> #5
>>> name = input("enter a name")
enter a name kiranganesh
>>> first_char = name[0]
>>> user_char = input("enter a char")
enter a char r
>>> final_name =name.replace(first_char,user_char)
>>> print(final_name)
 rkiranganesh
>>> #6 repeated item of list
>>> numbers = [1,4,3,2,4,2]
>>> num =[]
>>> for i in numbers:
	if i not in nums:
		nums.append(i)
		else:
			
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> for  i in numbers:
	if i not in nums:
		nums.append(i)
	else:
		print(i,end="")

		
Traceback (most recent call last):
  File "<pyshell#66>", line 2, in <module>
    if i not in nums:
NameError: name 'nums' is not defined
>>> #7
>>> elements =[1,2,3]
>>> sum=0
>>> for i in elements:
	sum=sum+i

	
>>> print(sum)
6
>>> user_value = int(input("enter a number "))
enter a number 10
>>> devidin_number = sum/user_ value
SyntaxError: invalid syntax
>>> deviding_number = sum/user_value
>>> print(deviding_number)
0.6
>>> #8
>>> given_numbers=[1,2,2]
>>> addition =0
>>> for i in given_numbers:
	addition = addition+i

	
>>> print("addition",addition)
addition 5
>>> length = len(given_numbers)
>>> mean = addition/length
>>> print("mean :",mean)
mean : 1.6666666666666667
>>> given_numbers.sort()
>>> if length%2==0:
	median1 = given_numbers[length//2]
	median2 = given_numbers[length//2-1]
	median = (median1+median2)/2
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> 
>>> if length%2 ==0:
	median1 = given_numbers[length//2]
	median2 = given_numbers[length//2-1]
	median=(median1+median2)/2
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> #9
>>> given_string="india
SyntaxError: EOL while scanning string literal
>>> #9
>>> given_string = "india"
>>> update_string = given_string.swapcase()
>>> print(update_string)
INDIA
>>> #10
>>> given_int =11
>>> binary = bin(given_int)
>>> print(binary)
0b1011
>>> octal = oct(given_int)
>>> print(octal)
0o13
>>> 