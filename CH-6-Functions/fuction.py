'''                                             FUNCTION IN PYTHON                                                '''

'''

BLOCK OF STATEMENT THAT PERFORMS A SPECIFIC TASK IS KNOWS AS FUNCTION.

1. Definition: A function is a block of organized, reusable code that only runs when it is specifically called.

2.Purpose: It prevents you from writing the same code over and over again (known as the DRY principle: 
Don't Repeat Yourself).It also breaks large programs into smaller, manageable, and modular chunks.

3.The def keyword: Every function definition must start with def.

4.Function Name: Follows def. It should be descriptive of what the function does
(e.g., calculate_total). Python convention is to use lowercase words separated by underscores.

5.Parentheses (): These come right after the name. They hold your inputs.
Even if your function takes no inputs, you still need empty parentheses ().

6.Colon :: This marks the end of the function's definition line and tells Python that 
the code block is about to start.

7.Indentation: All the code inside the function must be indented (usually 4 spaces). 
Python relies on indentation to know what code belongs to the function.

8. we also use f(x) to reduce redundancy(it means writing the exact same code or logic in multiple places.)

'''
#====================================================================================================================================================

'''SYNTAX OF FUNCTION'''

'''
 
def func_name(parameter1,parameter2..):    #parameter: (input)name if the variable
 #some work 
 return val 

func_name(arg1,arg2..)# function call.     #argument: 

'''
#=======================================================================================================================================================

''' Calculate sum of a & b function '''

def calc_sum(a,b): #Here we made that a f(x) while coding so we don't have to use same thing for 5 to 4 times 
    sum = a+b    # f(x) == function 
    print(sum)   # FUNCTION DEFINITION
    return sum 

calc_sum(5,6)  # called out the f(x) and it's done FUNCTION CALL
calc_sum(7,9)
calc_sum(5,44)
calc_sum(7889,7923)

#=======================================================================================================================================

''' Average of three numbers '''

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg 

calc_avg(1,2,6)
calc_avg(8,9,2)
calc_avg(88,90,45)


#==============================================================================================================================================

''' FUNCTION IN PY '''

''' BUILT-IN F(X) '''

print("hello world!","welcome") #sep = " "
print("python is a high level language") # end = /n 
len()
range()
type()

''' USER DEFINED FUNCTION '''

def calc_prod(a, b):
    mul = a * b
    print(mul)
    return mul

calc_prod(3,35)
#==================================================================================================================================================



























