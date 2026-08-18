#================================= LOOPS IN PYTHON ==========================================#
'''
1. loop is a block of code that is repeated until a certain condition is met.

2. there are two types of loops in python:
a. for loop
b. while loop

3. for loop is used to iterate over a sequence (list, tuple, string) or
other iterable objects.

4. while loop is used to execute a block of code as long as a certain condition is true.

5. break statement is used to exit a loop.

6. continue statement is used to skip the current iteration of a loop and move to 
the next iteration.

7. else statement can be used with loops to execute a block of code when the loop
is finished.

8. nested loops are loops inside loops.

9. infinite loops are loops that never end.

'''

#===============================================================================================================

''' while loop '''

while 2 == 2: # this line will print hello infinite times cause 2 is always equal to 2 and loop keeps on going 
    print("hello")

# another example 

count = 1 # here, we have given condition that in 1 print hello world until and add +1 while performing the output
while count <= 5 :
    print ("hello world")
count = 1+count 
print(count)

#===========================================================================================================================

'''ITERATORS'''

i = 1 
while count <=5:
    print("hello world")
    i+=1



 # print num 1 to 5 

i = 5 
while  i <= 5:
    print (i)
    i+=1
print("loop ended")

#=============================================================================================================================

'''BREAK IN WHILE LOOP'''

'''break: used to terminate the loop when encountered'''

i=1
while i<=5:
    print()
    if(i==3):
        break
    i +=1  
    print("end of loop") 

#==================================================================================================================================================
'''CONTINUE IN WHILE LOOP'''

''' continue : terminates execution in the current iteration and continues execution of the loop
with the next iteration. '''

i = 0 
while i<= 5:
    if (i == 3):
        i += 1 
        continue #skip 
    print(i)
    i += 1

#=======================================================================================================================================================

'''FOR LOOP IN PYTHON'''

'''for loop : loops are used for sequential traversal. for traversing list,string,tuples etc.'''

# for loop syntax

veggies = ["potato","tomato","lady finger","brinjal"]

for val in veggies:
    print(val)

#for loop in tup 

tup=(1,2,3,4,5,6,7)
for num in tup :
    print(num)

# for loop in str

str=("negative pr")
for var in str:
    print(var)

#===========================================================================================================
''' for loop with else '''

list = [1,2,3]
for el in list :
    print(el)
else:
    print("END")

str = "hello by mac"

for char in str:
    print(char)
else:
    print("END")

 #============================================================================================================

'''RANGE FUNCTION'''

'''
range : range functions returns a sequence of numbers, starting from 0 (by default)
and increments by 1 (by default), an stops before a specified number.

'''

for el in range(5):
    print(el)

for el in range (1,5):
    print(el)

for el in range(1,5,2):
    print(el)      


seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

#=============================================================================================================================================

'''START?,STOP,STEP?'''

for i in range(10) : #range(stop)
    print(i)

for i in range(2,10): #range(start,stop)
    print(i)   

for i in range(2,10,2): #range(start,stop,step)
    print(i)

for i in range(2,101,2): # to print even num 
    print(i)

#=================================================================================================================================================

'''PASS STATEMENT'''

for i in range(5):
    pass
if i >5:
    pass
print("some useful work")
