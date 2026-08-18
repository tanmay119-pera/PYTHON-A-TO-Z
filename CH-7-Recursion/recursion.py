'''                                         RECURSION IN PYTHON                                                 '''
'''
#.                       WHEN A FUNCTION CALLS ITSELF REPEATEDLY IS KNOW AS RECURSION 

1.In simple terms, recursion is when a function calls itself to solve a smaller piece of the same problem.

2.The Base Case: This is the condition that tells the function to stop calling itself. 
Without a base case, your function will run forever (an infinite loop) until Python crashes with a RecursionError.

3.The Recursive Case: This is where the function calls itself, 
but with a modified argument that brings it one step closer to the base case.

4.Recursion Limit: Python has a built-in safety net to stop infinite recursion. By default, 
a function can only call itself about 1,000 times. If you exceed this, Python throws a
 RecursionError: maximum recursion depth exceeded. You can check or change this limit using the sys module 
 (sys.setrecursionlimit()), though it's rarely recommended unless you know exactly what you are doing.

5.No Tail-Call Optimization: Some languages optimize recursion so it uses less memory. 
Python's creator deliberately chose not to include this feature, meaning heavy recursion in
 Python can consume a lot of memory compared to a simple for or while loop (iteration).

6.Pros: It makes code much cleaner and easier to read for specific problems, especially when
 navigating complex data structures like trees, graphs, or directories.

Cons: It uses more memory because of the call stack, and it is usually slightly slower than using a 
standard iterative loop.

'''
#====================================================================================================================================================

''' print n to 1 backwards '''

def show(n):                
   if(n==0):        # BASE-CASE
      return         
   print(n)
   show(n-1)

show(4)
show(6)
show(9)


#=========================================================================================================================================================

''' RETURNS N! '''

def fact(n):
   if(n==0 or n==1):
      return 1
   else:
      return n * fact(n-1)
   
   print(6)
   print(7)
   print(4)


#============================================================================================================================================================

'''                                               LET'S PRACTICE                                                   '''

''' WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL '''


def calc_sum(n):
   if(n==0):
      return 0 
   return calc_sum(n-1)+n

sum = calc_sum(5)
print(5)

   
'''WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENT IN A LIST
( USE LIST & INDEX AS PARAMETER )'''

def print_list(list,idx=0):
   if(idx== len(list)):
      return
   print_list(list[idx])
   print_list(list,idx+1)


fruits = ["mango","berry","apple"]
print_list(fruits)