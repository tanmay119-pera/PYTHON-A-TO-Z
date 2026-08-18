# first problem

'''
store following words meaning in a python dictionary
table: "a piece of furniture"," "list of fact and figures" 
    cat: " a small animal "
'''

my_dict = {
  "table": ["a piece of furniture", "list of fact and figures"],
  "cat": ["a small animal"]
}
print(my_dict)

#===================================================================================================================================    

# second problem

'''you are given list of subjects for students. assume one classroom iis required for 1 subject.
 find out how many classrooms are required for the following subjects
 
 "python", "java", "c++", "python", "javascript", "java", "python" , "java" 
 , "c++" , "C"
 
 '''

subjects = ["python", "java", "c++", "python", "javascript", "java", "python" , "java" , "c++" , "C"]
unique_subjects = set(subjects)  # Convert the list to a set to get unique subjects
num_classrooms = len(unique_subjects)  # The number of unique subjects is the number of classrooms required
print(num_classrooms)  # Output: 5 (python, java, c++, javascript, C)

#===================================================================================================================================

# third problem

''' 
wap to enter marks of 3 subjects from the user and store them in a dictionary. 
start with an empty dictionary and add one by one. use subjects name as key and marks as value 
'''
#method 1
marks = {}  # Create an empty dictionary to store marks

x =int(input("Enter marks for phy: "))  # Get phy marks from the user
marks.update({"phy": x})  # Add phy marks to the dictionary

x=int(input("Enter marks for chem: "))  # Get chem marks from the user
marks.update({"chem": x})  # Add chem marks to the dictionary

x=int(input("Enter marks for math: "))  # Get math marks from the user
marks.update({"math": x})  # Add math marks to the dictionary

print(marks)  # Output: {'phy': 85, 'chem': 90, 'math': 88} (example output)



#method 2
marks = {}  
marks["math"] = int(input("Enter marks for math: "))  # Add math marks to the dictionary
marks["science"] = int(input("Enter marks for science: "))  # Add science marks
marks["english"] = int(input("Enter marks for english: "))  # Add english marks
print(marks)  # Output: {'math': 85, 'science': 90, 'english': 88} (example output)

#==========================================================================================================================================

# fourth problem

''' fig out a way to store 9 and 9.0 as separate
 values in the set. (you can use in built in data types) '''

my_set = {9, 9.0}  # This will store both 9 and 9.0 as separate values in the set
print(my_set)  # Output: {9, 9.0}
