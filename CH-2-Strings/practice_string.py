# wap to input user's name and print its length.

name = input("Enter your name: ")
name_length = len(name)
print("The length of your name is:", name_length) 

#=======================================================================================================================================================

# wap to find the occurrence of $ in a string.
str1 = ("7888$$","$$$","$$","$","$$$$$$","455$$")
occurrence = str1.count('$')
print("The occurrence of $ in the string is:", occurrence)

#======================================================================================================================================================

# wap grade of student based on marks marks >= 90: A,marks >= 80 and marks < 90: B,
# marks >= 70 and marks < 80: C, marks >= 60 and marks < 70: D, marks < 60: F.
marks = int(input("Enter the marks of the student: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80 and marks < 90:  
    grade = 'B'
elif marks >= 70 and marks < 80:
    grade = 'C'
elif marks >= 60 and marks < 70:
    grade = 'D'
else: 
    grade = 'F'
print("The grade of the student is:", grade)    

#======================================================================================================================================================

# wap to check if a number is even or odd.


num = int(input("Enter a number: "))
if num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 

#=======================================================================================================================================================    
 
# wap to find the largest of three numbers by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

#=======================================================================================================================================================

# wap to check if a year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#=======================================================================================================================================================    

# wap to check if a string is a palindrome or not.
str1 = input("Enter a string: ")
if str1 == str1[::-1]:
    print(str1, "is a palindrome.")
else:
    print(str1, "is not a palindrome.") 

#=======================================================================================================================================================

# wap to check if a string is a multiple by 7 or not.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(num, "is a multiple of 7.")
else:
    print(num, "is not a multiple of 7.")          

         

