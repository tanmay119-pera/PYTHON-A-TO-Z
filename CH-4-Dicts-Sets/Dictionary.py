#===================================== DICTIONARY ========================================================#
'''

1. A dictionary is a collection which is unordered, changeable and indexed.
 In Python dictionaries are written with curly brackets, and they have keys and values.
 
 2. Dictionary items are ordered, changeable, and do not allow duplicates.
 
 3. Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

 4. The values in dictionary items can be of any data type, and can be duplicated,
 but the keys must be of immutable data type (string, number or tuple with immutable elements) and must be unique.
 
 5. A dictionary can be created by using the built-in dict() function.

 6. Dictionary items are ordered, changeable, and do not allow duplicates.

 7. Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

 8. The values in dictionary items can be of any data type, and can be duplicated, but the keys 
 must be of immutable data type (string, number or tuple with immutable elements) and they must be unique. 

 '''

#===================================================================================================================================

''' create a dictionary '''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

#===================================================================================================================================

'''dictionary can store any data type as value but keys must be of immutable data type and unique'''

school = {
  "name": "ABC School",
  "location": "New York",
  "students": 500,
  "is_public": True,
  "subjects": ["Math", "Science", "History"],
  "principal": {"name": "John Doe", "age": 50}
}
print(school)

#===================================================================================================================================

'''accessing dictionary items'''

print(car["brand"])  # Output: Ford 
print(school["name"])  # Output: ABC School
print(school["principal"]["name"])  # Output: John Doe

#===================================================================================================================================

'''changing values in a dictionary'''

car["year"] = 2020
print(car)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
school["students"] = 550
print(school)  # Output: {'name': 'ABC School', 'location': 'New York', 'students': 550, 'is_public': True, 'subjects': ['Math', 'Science', 'History'], 'principal': {'name': 'John Doe', 'age': 50}}

#===================================================================================================================================

'''adding items to a dictionary'''

car["color"] = "red"
print(car)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}
school["teachers"] = 10
print(school)  # Output: {'name': 'ABC School', 'location': 'New York', 'students': 550, 'is_public': True, 'subjects': ['Math', 'Science', 'History'], 'principal': {'name': 'John Doe', 'age': 50}, 'teachers': 10}

#===================================================================================================================================

'''removing items from a dictionary'''

del car["model"]
print(car)  # Output: {'brand': 'Ford', 'year': 2020, 'color': 'red'}
school.pop("is_public")
print(school)  # Output: {'name': 'ABC School', 'location': 'New York', 'students': 550, 'subjects': ['Math', 'Science', 'History   '], 'principal': {'name': 'John Doe', 'age': 50}, 'teachers': 10}   

#===================================================================================================================================

''' null value in dictionary '''

null_dict = {}
null_dict["name"]
print(null_dict)  # Output: {}

''' entering null value in dictionary  '''

null_dict = {}
null_dict["name"] = "Tanmay"
print(null_dict)  # Output: {'name': 'Tanmay'}

#===================================================================================================================================

'''key value pair in dictionary''' # aka nested dictionary

student = {
  "name": "Aunshka",
  "subject": {
    "maths": "98",
    "science": "95",
    "english": "92",
    "history": "90"
  }
} 
print(student)  # Output: {'name': 'Aunshka', 'subject': {'maths': '98', 'science': '95', 'english': '92', 'history': '90'}}

#===================================================================================================================================

'''dictionary methods'''

my_dict = {
  "name": "Alice", 
  "age": 30,
  "city": "New York"
}

my_dict.clear()  # Removes all items from the dictionary    
print(my_dict)  # Output: {}

my_dict.keys()  # Returns a view object containing the keys of the dictionary
print(my_dict.keys())  # Output: dict_keys([])

my_dict.values()  # Returns a view object containing the values of the dictionary   
print(my_dict.values())  # Output: dict_values([])

my_dict.items()  # Returns a view object containing the key-value pairs of the dictionary as tuples
print(my_dict.items())  # Output: dict_items([])

my_dict.get("name")  # Returns the value of the specified key, or None if the key does not exist    
print(my_dict.get("name"))  # Output: Alice

my_dict.pop("age")  # Removes the specified key and returns its value, or raises a KeyError if the key does not exist
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New    York'}

my_dict.update({"country": "USA"})  # Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}    

#===================================================================================================================================




