'''                                       INTRODUCTION TO PYTHON                                              '''



#### This is a simple Python program that prints "Hello, World!" to the console ####
print("Hello, World!")

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### for variables and values ####
name = "Tanmay"
age = 18
print(name,age)

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### for input and output ####


name = input("Enter your name: ")
print("Hello, " + name + "!") 

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### DATA TYPES #### 

x =69
y=3.14
z=True
print(type(x))
print(type(y))
print(type(z))

#--------------------------------------------------------------------------------------------------------------------------------------------------

#### float data type #### 
f=69.9

#==================================================================================================================================================

### string data type ###

str ="This is a string."

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### boolean data type ####

b=False
print(type(f))
print(type(str))
print(type(b))

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### arithmetic operations ####

a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### expression and execution ####
a,b = 10, 5
Txt = "@"
print(10*Txt*5) # This will print the string "@" repeated 50 times (10 * 5 = 50)

#-------------------------------------------------------------------------------------------------------------------------------------------------

c,d = "2", 3
Txt = "@"
print((c+Txt)*d) # This will concatenate the string "2" with "@" to get "2@", and then repeat it 3 times to get "2@2@2@"


#-------------------------------------------------------------------------------------------------------------------------------------------------

e,f = 2, 3
g = 4 
print(e+f*g) # This will first calculate the multiplication (3 * 4 = 12) and then add it to 2 to get 14

#------------------------------------------------------------------------------------------------------------------------------------------------

ax,bx = 10, 5.0
zx = ax*bx
print(zx) # This will multiply the integer 10 with the float 5.0

#------------------------------------------------------------------------------------------------------------------------------------------------

ay,by = 1,2
zy=ay/by 
print(zy) # This will divide the integer 1 by the integer 2, resulting in a float value of 0.5

#------------------------------------------------------------------------------------------------------------------------------------------------

az,bz = 1.5,3
zz=az//bz
print(zz) # This will perform floor division on the float 1.5 by the integer 3, resulting in 0.0

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b=12,5
c=a//b
print(c) # This will perform floor division on the integer 12 by the integer 5

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b=-12,5
c=a//b
print(c) # This will perform floor division on the integer -12 by the integer 5

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b = 12,-5
c=a//b
print(c) # This will perform floor division on the integer 12 by the integer -5

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b= -5,2
c=a%b
print(c) # This will calculate the modulus of -5 by 2, resulting in

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b=5,2
c=a%b
print(c) # This will calculate the modulus of 5 by 2, resulting in

#------------------------------------------------------------------------------------------------------------------------------------------------

a,b=-5,-2
c=a%b
print(c) # This will calculate the modulus of -5 by -2, resulting in -

#------------------------------------------------------------------------------------------------------------------------------------------------

#### COMMENTS ####

# This is a single-line comment in Python.

"HELLO" # This is an inline comment in Python.

#=================================================================================================================================================

#### INPUT IN PYTHON ####

##string input##
name = input("Enter your name: ")
print("Hello, " + name + "!")   

#================================================================================================================================================

##integer input##

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")       

#=================================================================================================================================================

##float input##

height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")  

#------------------------------------------------------------------------------------------------------------------------------------------------

### taking input from the user ###

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))  
print("Hello, " + name + "! You are " + str(age) + " years old and your height is " + str(height) + " meters.")

#========================================================================================================================================

#### conditional statements #### 
a,b = 22,30
if a > b:               #condition 1
    print("a is greater than b") #statement 1 
elif a < b:             #condition 2
    print("a is less than b")  #statement 2
else:
    print("a is equal to b") #statement N 

#one more example of conditional statements
light = input("Enter the traffic light color (red, yellow, green): ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Caution")
elif light == "green":
    print("Go")     
else:
    print("traffic light is broken")    

# practice problem on conditional statements
# # 'print output for a = 5 and g = m 
# a= 2 and g = f '''
a= int(input("a: "))
g= input("m/f: ")
if ((a == 1 or a ==2 ) and g == "m"):
    print("fee is 100")
elif ((a == 3 or a ==4 ) and g == "f"):   
   print("fee is 200")
elif ((a == 5 ) and g == "m"):    
    print("fee is 300")
else:
    print("no fee is required")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------    
### conditional statements ###

# single line if ("ternary operator")#

food = input("Enter a food item: ")
result = "Yummy!" if food == "pizza" else "Not my favorite." # <val1> if <condition> else <val2>
print(result)

food = input("Enter a food item: ")
print("Yummy!" if food == "pizza" else "Not my favorite.") # <stt1> if <condition> else <stt2>

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#clever if / ternary operator#

age = int(input("Enter your age: "))
vote  = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(vote)

#<var> = (false_value, true_value)[<condition>]

salary = int(input("Enter your salary: "))
tax_rate = (0.2, 0.3)[salary > 50000]
print("Tax rate:", tax_rate)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

### BEST PRACTICES TO REPRESENT THE CODE###

# 1. Use meaningful variable names
# 2. Use comments to explain the code
# 3. Follow consistent indentation
# 4. Avoid using global variables   
# 5. Use functions to organize code into reusable blocks
# 6. Handle exceptions and errors gracefully
# 7. Keep the code simple and readable  
# 8. Use version control systems for collaborative projects
# 9. Write unit tests to ensure code correctness
# 10. Continuously refactor and improve the code for better performance and maintainability

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

##################### END OF FIRST CHAPTER #####################