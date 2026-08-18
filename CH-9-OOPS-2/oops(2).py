'''                          OOPS PART 2                               '''

''' del KEYWORD 
used to delete objects properties or object itself

del s1.name
del s1
'''
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"   # Readable output

    def __del__(self):
        print(f"Object for '{self.name}' has been deleted")  # Deletion hook

s1 = Student("alex")
print(s1)          

del s1           # triggers del function

try:  
    print(s1)
except NameError:
    print("s1 no longer exists")

#=============================================================================================================
'''
PRIVATE(LIKE) ATTRIBUTES AND METHODS!
Conceptual implementation in python.

private attributes and methods are meant to be used only within the class and 
are not accessible from outside the class.


'''
# example 1

class Person:
    __name = "anonymous"
   

p1 = Person()
print(p1.__name)

#example 2

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass       # Private attribute

    def reset_pass(self):
        return self.__acc_pass           

acc1 = Account("435367265", "rt4564")

print(acc1.acc_no)                       
print(acc1.reset_pass())    

''' here we can see the password just got printed and showing no error '''

#==========================================================================================================================================================================
'''
INHERITANCE (3RD PILLAR OF OOPS IN PY)

When on class(child/derived)derives the properties and methods of another class 
(parent/base).
'''

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())

'''
TYPES OF INHERITANCE 

1. SINGLE INHERITANCE

2. MULTI-LEVEL INHERITANCE 

3. MULTIPLE INHERITANCE 

 BASE  =   DERIVED  =  DERIVED 
(PARENT) (CHILD-PAR)   (CHILD)
'''
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand 

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

'''
 BASE1 = BASE2 = DERIVED
(PAR-1) (PAR-2) (CHILD)

'''

class a:
    varA = "welcome to class A"

class b:
    varB = "welcome to class B"

class c(a, b):                   
    varC = "welcome to class C"

c1 = c()

print(c1.varC)                  
print(c1.varB)                   
print(c1.varA)                   

#==============================================================================================================================================

'''
SUPER METHOD
super() method is used to access methods of the parent class.
'''
class Car:
    def __init__(self,type):
        self.type = type 

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name 
        super().__init__(type)   # using super()
        super().start

car1 = ToyotaCar("prius","electric")
print(car1.type)

#===============================================================================================================================================================================================
'''
CLASS METHOD 
"A class method is bound to the class and receives the class as an implicit first argument.
note - static method can't access or modify class state and generally for utility.

class Student:
    @classmethod #decorator
    def college(cls):
        pass 
'''
# Method 1
class Person:
    name = "anonymous"

    def changeName (self,name):
        self.name = name 

p1 = Person()
p1.changeName("alex")
print(p1.name)
print(Person.name) # add anything like Person.name

# Method 2
class Person:
    name = "anonymous"

    def changeName (self,name):
        self.__class__.name = "alex" # add self.__class__

p1 = Person()
p1.changeName("alex")
print(p1.name)
print(Person.name)

# @classmethod 
class Person:
    name = "anonymous"

    def changeName (self,name):
        self.name = name 

p1 = Person()
p1.changeName("alex")
print(p1.name)
print(Person.name)

#==========================================================================================================================

'''PROPERTY
We use @property decorator on any method in the class to use the method as a property.
'''

# example 
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths 
        self.percentage = str((self.phy+self.chem+self.maths)/3)+"%"

   # def calcPercentage(self):
       # self.percentage = str((self.phy+self.chem+self.maths)/3)+"%"
    '''we can do this we can use @property'''


    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"


stud1 = Student(98,97,99)
print(stud1.percentage)

stud1 = 86
print(stud1.percentage)

#=========================================================================================================================================================
'''
POLYMORPHISM : OPERATOR OVERLOADING

When the same operator is allowed to have different meaning according to the context 

operator & dunder functions 

a+b  #addition             a. __add__(b)

a-b  #subtraction          a. __sub__(b)

a*b  #multiplication       a. __mul____(b)

a/b  #division.            a. __truediv____(b)

a%b  #addition             a. __mod___(b)
 '''

#ADD OPERATOR 

print (1+2)#addition
print("hello"+"world")#concatenation
print([1,2,3]+[4,5,6])#merge

''' COMPLEX NUMBERS '''

'''A complex number has two parts — a real part and an imaginary part. 
The imaginary part uses the letter i, but in Python we write it as j. 
So a complex number looks like 3 + 4j.

Creating complex numbers in Python:
python
c = 3 + 4j
print(c)  # Output: (3+4j)


Key points:

Real part — the normal number. Imaginary part — the number with j at the end. When you 
add them together, you get a complex number.

Accessing parts:

c = 3 + 4j
print(c.real)  # 3.0
print(c.imag)  # 4.0

c1 = 2 + 3j
c2 = 1 + 2j
print(c1 + c2)  # (3+5j)
print(c1 * c2)  # (-4+7j)   
'''
class Complex:
    def __init__(self,real,img):
        self.real = real 
        self.img = img 
    
    def showNumber(self):
        print(self.real,"i+","self.img","j")

    def __add__(self,num2):                  # Dunder_Function for ADDITION 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):                  # Dunder_Function for subtraction 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __mul__(self,num2):                  # Dunder_Function for multiplication
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __truediv__(self,num2):              # Dunder_Function for division
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
    def __mod__(self,num2):                  # Dunder_Function for percentage
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    

num1= Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1-num2
num3.showNumber()

num3 = num1*num2
num3.showNumber()

num3 = num1/num2
num3.showNumber()

num3 = num1%num2
num3.showNumber()