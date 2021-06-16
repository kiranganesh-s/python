Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[]
>>> numbers.append(1)
>>> print('list after appending element:',numbers)
list after appending element: [1]
>>> numbers.insert(1,2)
>>> print('list after inseting element:',numbers)
list after inseting element: [1, 2]
>>> list2=[3,4,5]
>>> numbers.extend(list2)
>>> print('list after extending:',numbers)
list after extending: [1, 2, 3, 4, 5]
>>> #deleting elements using pop,remove,del
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> numbers.pop(3)
4
>>> print('list after poping:',numbers)
list after poping: [1, 2, 3, 5]
>>> numbers.remove(5)
>>> print('list after removing:',numbers)
list after removing: [1, 2, 3]
>>> del numbers[0:]
>>> print('list after deleting: ',numbers)
list after deleting:  []
>>> #finding min and max values
>>> values =[2,3,6,1,4]
>>> minimum_value=min(values)
>>> print('minimum value is:',minimum_value)
minimum value is: 1
>>> maximum_value=max(values)
>>> print('maximum value is:',maximum_value)
maximum value is: 6
>>> #reversing tuple
>>> def reverse(nums):
	new_tup =()
	for i in reversed(nums):
		new_tup = new_tup+ (i,)
		print(new_tup)

		
>>> nums=(1,2,3,4)
>>> reverse(nums)
(4,)
(4, 3)
(4, 3, 2)
(4, 3, 2, 1)
>>> #converting tuple to list
>>> values=[2,3,4,5]
>>> alist=list(values)
>>> print(alist)
[2, 3, 4, 5]
>>> 