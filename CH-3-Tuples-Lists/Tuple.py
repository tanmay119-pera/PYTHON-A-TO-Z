#=========================== Tuple.py ===============================#
'''
1.tuple is a immutable sequence type, which means that 
once a tuple is created, its contents cannot be changed.

2.Tuples are defined by enclosing the elements in parentheses () 
and separating them with commas.

3.Tuples can contain elements of different types, 
including other tuples.

4.Tuples are often used to group related data together,and 
they can be used as keys in dictionaries because they are "immutable".

5.Tuples support indexing and slicing, just like lists, 
but they do not support item assignment.

6.Tuples can be created with a single element by 
including a comma after the element,
'''

#==================================================================================================

''' creating a tuple '''

tup1 = (1, 2, 3, 4, 5)
print(tup1)  # Output: (1, 2, 3, 4, 5)
print(type(tup1))  # Output: <class 'tuple'>
print(len(tup1))  # Length of the tuple
print(tup1[0])  # Accessing the first element
print(tup1[1:4])  # Slicing the tuple to get a sub-tuple

#===================================================================================================

''' creating a tuple with a single element '''

single_element_tuple = (42,)  # Note the comma after the element
print(single_element_tuple)  # Output: (42,) 
print(type(single_element_tuple))  # Output: <class 'tuple'>

#===================================================================================================

''' creating a tuple without parentheses '''

another_single_element_tuple = 42,  # Note the comma after the element
print(another_single_element_tuple)  # Output: (42,)
print(type(another_single_element_tuple))  # Output: <class 'tuple'>

#===================================================================================================

''' slicing a tuple '''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:5])  # Output: (3, 4, 5)
print(numbers[:4])   # Output: (1, 2, 3, 4)
print(numbers[5:])   # Output: (6, 7, 8, 9)
print(numbers[-3:])  # Output: (7, 8, 9)

#===================================================================================================

''' tuples are immutable '''

my_tuple = (1, 2, 3)
# my_tuple[1] = 42  # This will raise a TypeError because tuples are immutable

#===================================================================================================

''' tuple methods '''
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple.count(2))  # Output: 1 (counts the number of occurrences
print(my_tuple.index(3))  # Output: 2 (returns the index of the first occurrence)


