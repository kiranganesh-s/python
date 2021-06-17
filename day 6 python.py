Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> capitals={'Ap':'"Hyderabad','Tamilnadu':'Chennai'}
>>> capital={'maharashtra':'mumbai','Goa':'panaji'}
>>> print('merging two dictionaries:',capitals.update(capital))
merging two dictionaries: None
>>> print(capitals)
{'Ap': '"Hyderabad', 'Tamilnadu': 'Chennai', 'maharashtra': 'mumbai', 'Goa': 'panaji'}
>>> #updating key value pair
>>> capitals['Tamilnadu']='Madras'
>>> print(capitals)
{'Ap': '"Hyderabad', 'Tamilnadu': 'Madras', 'maharashtra': 'mumbai', 'Goa': 'panaji'}
>>> #removing element using pop function
>>> print('remove element:',capitals.pop('Ap'))
remove element: "Hyderabad
>>> print('after removing element using pop func:',capitals)
after removing element using pop func: {'Tamilnadu': 'Madras', 'maharashtra': 'mumbai', 'Goa': 'panaji'}
>>> #remove element using popitem function
>>> print('remove element:',capitals.popitem())
remove element: ('Goa', 'panaji')
>>> print('after removing element using popitem:',capitals)
after removing element using popitem: {'Tamilnadu': 'Madras', 'maharashtra': 'mumbai'}
>>> #teo lists into dictionary
>>> #two lists into dictionary
>>> test_keys=['raj', 'ram']
>>> test_values=[ 1,2]
>>> print('keys as:',str(test_keys))
keys as: ['raj', 'ram']
>>> print('values as:',str(test_values))
values as: [1, 2]
>>> result=dict(zip(test_keys,test_values))
>>> print(str(result))
{'raj': 1, 'ram': 2}
>>> #length of set
>>> numbers={1,2,4,5}
>>> print('length of set:',len(numbers))
length of set: 4
>>> set1={1,2,4,5}
>>> set2={11,22,33,44,55}
>>> set3=(set1.union(set2))
>>> print('insertion of set1 and set2 is:',set3)
insertion of set1 and set2 is: {1, 2, 33, 4, 5, 11, 44, 22, 55}
>>> print('removing set2 elements:')
removing set2 elements:
>>> set2={11,22,33,44,55}
>>> for i in set2:
	set3.remove(i)

	
>>> print('after removing set2 from set3:',set3)
after removing set2 from set3: {1, 2, 4, 5}
>>> 