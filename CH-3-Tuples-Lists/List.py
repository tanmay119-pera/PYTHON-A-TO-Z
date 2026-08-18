#======================== LIST PYTHON ================================#
'''
1. Lists are mutable sequence types, which means that their contents 
can be changed after they are created.

2. Lists are defined by enclosing the elements in square brackets [] 
and separating them with commas.

3. Lists can contain elements of different types, 
including other lists.

4. Lists are often used to store collections of related data, 
and they can be modified by adding, removing, or changing elements.

5. Lists support indexing and slicing,which allows 
you to access and manipulate specific elements or subsists.

6. Lists can be created with a single element by including
a comma after the element, but it is not necessary like in tuples.

7. Lists have a variety of built-in methods for manipulating their 
contents,such as append(), extend(), insert(), remove(), pop(), 
and sort().

8. Lists are commonly used in Python for tasks such as storing data,
iterating over collections, and implementing various data structures.

'''

#===========================================================================================

''' creating a list '''

marks = [56.7, 78.9, 90.5, 65.4] 
print(marks) # Output: [56.7, 78.9, 90.5, 65.4]
print(type(marks)) # Output: <class 'list'>
print(len(marks)) # Length of the list
print(marks[0])  # Accessing the first element
print(marks[1:3])  # Slicing the list to get a sublist  

#==============================================================================================

''' slicing a list '''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Output: [3, 4, 5]
print(numbers[:4])   # Output: [1, 2, 3, 4]
print(numbers[5:])   # Output: [6, 7, 8, 9]
print(numbers[-3:])  # Output: [7, 8, 9]    

#===============================================================================================

''' modifying a list '''    

fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'  # Modifying the second element
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

#===============================================================================================================

''' list methods '''

fruits = ['apple', 'banana', 'cherry']

fruits.append('orange')  # Adding a new element to the end of the list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

fruits.insert(1, 'grape')  # Inserting an element at a specific index
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']

fruits.remove('cherry')  # Removing an element by value
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'orange']

popped_fruit = fruits.pop()  # Removing the last element and returning it
print(popped_fruit)  # Output: 'orange'
print(fruits)  # Output: ['apple', 'grape', 'blueberry']

fruits.sort()  # Sorting the list in place      
print(fruits)  # Output: ['apple', 'blueberry', 'grape']    

fruits.reverse()  # Reversing the order of the list
print(fruits)  # Output: ['grape', 'blueberry', 'apple']

fruits.clear()  # Removing all elements from the list
print(fruits)  # Output: [] 

fruits.reverse() # Reversing an list with elements
print(fruits)  # Output: [cherry,banana,apple] 

#===============================================================================================================


