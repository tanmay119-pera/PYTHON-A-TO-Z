#=============================== SETS =====================================================#
'''
1. A set is a collection which is unordered, unchangeable, and unindexed. 
In Python sets are written with curly brackets.

2. Set items are unordered, unchangeable, and do not allow duplicates.

3. Set items are unindexed, so you cannot access them by referring to an index or a key.

4. Set items are unchangeable, but you can remove items and add new items.  

5. Sets are written with curly brackets, and each item is separated by a comma.

6. A set can be created by using the built-in set() function.

7. Set items are unordered, unchangeable, and do not allow duplicates.  

8. Set items are unindexed, so you cannot access them by referring to an index or a key.

9. Set items are unchangeable, but you can remove items and add new items.

10. Sets are written with curly brackets, and each item is separated by a comma.

11. A set can be created by using the built-in set() function.

12. in a set we can  store boolean values, numbers, strings, floats, integers and tuples 
but we cannot store lists, dictionaries or other sets because they are unhashable 
(mutable) data types.

13. sets are mutable but the elements inside the set must be of immutable 
 data type (string, number, tuple with immutable elements) and they must be unique.    
'''
#===================================================================================================================================

''' create a set '''

my_set = {"apple", "banana", "cherry"}  
print(my_set)

#===================================================================================================================================

''' sets do not allow duplicates '''

my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # Output: {'apple', 'banana', 'cherry'}

set2 = {1,2,2,2,2} # repeated item will be ignored during output
print(set2)  # Output: {1, 2}

#===================================================================================================================================

''' sets are unindexed, so you cannot access items by referring to an index or a key '''

my_set = {"apple", "banana", "cherry"}
# print(my_set[0])  # This will raise a TypeError

#===================================================================================================================================

''' methods for set manipulation '''

my_set = {"apple", "banana", "cherry"}

my_set.add("orange")  # Adds an item to the set
print(my_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

my_set.remove("banana")  # Removes an item from the set 
print(my_set)  # Output: {'apple', 'cherry', 'orange'}

my_set.clear()  # Removes all items from the set
print(my_set)  # Output: set()

my_set.pop()  # Removes a random item from the set and returns it
print(my_set)  # Output: set() (the set is now empty)


#===================================================================================================================================

''' syntax for empty set '''

collection = set()  # This creates an empty set  
print(collection)  # Output: set()

''' if we use empty curly brackets it will create an empty dictionary instead of a set '''

collection = {}  # This creates an empty dictionary, not a set
print(collection)  # Output: {}

#===================================================================================================================================

'''len function in set '''

collection = set()
collection.add("1")
collection.add("2")
collection.add("3")
collection.add("3")  # Duplicate item will be ignored
collection.add("4")
print(len(collection))  # Output: 4

#=====================================================================================================================================

''' sets operations '''

''' # union of sets # '''

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

union_set = set1.union(set2)  # Returns a new set that is the union of set1 and set2
print(union_set)  # Output: {'a', 'b', 'c', '   d', 'e'}    

''' The union of two sets is a set containing all the elements of both sets. The union of sets can be performed using the union() method or the | operator. '''  

#===================================================================================================================================

''' # intersection of sets # '''

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}      
intersection_set = set1.intersection(set2)  # Returns a new set that is the intersection of set1 and set2
print(intersection_set)  # Output: {'c'}

''' The intersection of two sets is a set containing only the elements that are common 
to both sets. The intersection of sets can be performed using the intersection() 
method or the & operator. '''

#===================================================================================================================================

''' # difference of sets # '''  

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
difference_set = set1.difference(set2)  # Returns a new set that is the difference of set1 and set2
print(difference_set)  # Output: {'a', 'b'}

''' The difference of two sets is a set containing the elements that are in the first set
 but not in the second set. The difference of sets can be performed using 
 the difference() method or the - operator. '''

