###========================================***STRING***============================================================== ###

'''' string is a data type in Python that represents a sequence of characters. It is used to store and manipulate text. 
Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
 They can contain letters, numbers, symbols, and whitespace characters.
'''

###================================================================================================================== ###

### basic operations with strings ###

# Concatenation: Joining two or more strings together using the + operator.
"Hello, " + "world!"  # Output: 'Hello, world!'

str1= "Hello"
str2= "world"
final_str = str1+ " " + str2
print(final_str) # Output: Hello world

#=========================================================================================================================================================
 
# length: Getting the number of characters in a string using the len() function.
len("Hello")  # Output: 5   

str1 = "god is great"
print(len(str1)) # Output: 13 (excluding spaces) 
 
#========================================================================================================================================================

# escape sequences: Using backslashes to include special characters in a string.

str1 = "this is a string.\nwe are creating in python programming" 
print(str1) # Output:
# this is a string.
# we are creating in python programming.so now we know that \n is used to create a new line in the string. 

#========================================================================================================================================================

# indexing: Accessing individual characters in a string using their position (index).
#.      01234  
str1 = "Hello"
#     -(54321)

print(str1[0])  # Output: 'H' (first character)
print(str1[1])  # Output: 'e' (second character)
print(str1[-1]) # Output: 'o' (last character)          

# few more examples of indexing

# example 1
#.      012 3 4567
str1 = "God's plan" 
#     -(876 5 4321)
print(str1[0])  # Output: 'G' (first character)
print(str1[4])  # Output: 's' (fifth character)
print(str1[-1]) # Output: 'n' (last character)
print(str1[-5]) # Output: 'p' (fifth character from the end) 

# example 2
#.      012345
str2 = "Python"
#     -(654321)
chr1 = str2[0]  # 'P'
chr2 = str2[3]  # 'h'
chr3 = str2[-1] # 'n'   
print(chr1) # Output: 'P'
print(chr2) # Output: 'h'
print(chr3) # Output: 'n'


#==================================================================================================================================================

## slicing: Extracting a portion of a string using a range of indices or we can say accessing part of the string using a range of indices. 
# str[starting index: ending index]  # Output: substring from starting index to ending index (excluding the character at the ending index) 

str1 = "Hello, world!"
print(str1[0:5])  # Output: 'Hello' (characters from index 0 to 4)
print(str1[7:12]) # Output: 'world' (characters from index 7 to 11)
print(str1[:5])   # Output: 'Hello' (characters from the beginning to index 4)
print(str1[7:12]) # Output: 'world!' (characters from index 7 to 11)
print(str1[1:])   # Output: 'world!' (characters from index 7 to the end)

# more example of slicing
# example 1
str2 = "royal challenger bangalore"
print(str2[0:5])   # Output: 'royal' (characters from index 0 to 4)
print(str2[6:15])  # Output: 'challenger' (characters from index 6 to 14)
print(str2[16:25]) # Output: 'bangalore' (characters from index 16 to 24)
print(str2[:5])    # Output: 'royal' (characters from the beginning to index 4)
print(str2[6:])    # Output: 'challenger bangalore' (characters from index 6 to the end)   

# example 2
str3 = "python programming"
print(str3[0:6])   # Output: 'python' (characters from index 0 to 5)
print(str3[7:18])  # Output: 'programming' (characters from index 7 to 17)
print(str3[:6])    # Output: 'python' (characters from the beginning to index 5)
print(str3[7:])    # Output: 'programming' (characters from index 7 to the end) 
print(str3[0:18])  # Output: 'python programming' (characters from index 0 to 17)

#===========================================================================================================================================================================================================================================================

## string functions: Python provides various built-in functions to manipulate strings, 
# such as upper(), lower(), strip(), split(), join(), replace(), find(), and more.

str = "I am a coding enthusiast."

#str.endswith("enthusiast."): This function returns True if the string ends with the specified suffix "enthusiast.", and False otherwise. In this case, since the string does indeed end with "enthusiast.", the output will be True.
print(str.endswith("enthusiast.")) # Output: True

#str.startswith("I am"): This function returns True if the string starts with the specified prefix "I am", and False otherwise. In this case, since the string does indeed start with "I am", the output will be True.
print(str.startswith("I am")) # Output: True    

#str.upper(): This function converts all characters in the string to uppercase. The output will be "I AM A CODING ENTHUSIAST.".
print(str.upper()) # Output: "I AM A CODING ENTHUSIAST."    

#str.lower(): This function converts all characters in the string to lowercase. The output will be "i am a coding enthusiast.".
print(str.lower()) # Output: "i am a coding enthusiast."

#str.capitalize(): This function capitalizes the first character of the string and converts the rest to lowercase. The output will be "I am a coding enthusiast.".
print(str.capitalize()) # Output: "I am a coding enthusiast."

#str.replace("coding", "programming"): This function replaces all occurrences of the substring "coding" with "programming" in the string. The output will be "I am a programming enthusiast.".
print(str.replace("coding", "programming")) # Output: "I am a programming enthusiast."  

#str.find ("coding"): This function returns the lowest index of the substring "coding" in the string. If the substring is not found, it returns -1. In this case, since "coding" is found at index 7, the output will be 7.
print(str.find("coding")) # Output: 7

#str.split(): This function splits the string into a list of substrings based on whitespace by default. The output will be ['I', 'am', 'a', 'coding', 'enthusiast.'].
print(str.split()) # Output: ['I', 'am', 'a', 'coding', 'enthusiast.']

#str.count("a"): This function counts the number of occurrences of the substring "a" in the string. The output will be 2, as there are two occurrences of "a" in the string.
print(str.count("a")) # Output: 2   

#==================================================================================================================================================================================================================================================

# conditional statements with strings: We can use conditional statements (if, elif, else) to perform different actions based on the content of a string.

age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")     

# nested if statements with strings: We can also use nested if statements to check multiple conditions within a string.

age = int(input("Enter your age: "))
if(age >= 18):
    if age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")