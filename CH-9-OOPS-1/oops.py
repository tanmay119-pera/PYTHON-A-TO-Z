'''                                         OOPS IN PYTHON                                                        '''
'                                    (OBJECT ORIENTED PROGRAMMING)                                                                                                   '
'''
TO MAP WITH REAL WORLD SCENARIOS, WE STARTED USING OBJECTS IN CODE.THIS IS CALLED ("OBJECT ORIENTED PROGRAMMING").

"procedural = functional(low redundancy and high reusability)= object oriente programming" 




1. Class & Object

A class is like a blueprint or template. For example, a "Car" blueprint defines what a car has
(color, brand) and what it can do (drive, stop). An object is the actual car built from that blueprint. 
You can create many objects from one class, each with different values.

2. __init__ (Constructor)

This is a special method that runs automatically when you create an object.
It is used to set up initial values for the object. Think of it like filling out a form when you register
— it captures your details the moment you sign up.

3. self

self simply means "this object itself." When a method is called on an object, 
Python needs to know which object it belongs to. self carries that reference.
 It's always the first parameter in instance methods.

4. Encapsulation

Encapsulation means keeping data safe inside a class and not allowing outside code to directly change it. 
You protect sensitive data using private variables (with __) and provide controlled access through methods.
Like a capsule — medicine is protected inside, you can't touch it directly.

5. Inheritance

Inheritance means a child class can use everything from a parent class without rewriting it. 
Like a child inheriting traits from parents. For example, an "Animal" class has a speak() method.
 A "Dog" class that inherits from Animal gets that method automatically, and can also add its own.

6. Multiple Inheritance

Python allows a class to inherit from more than one parent class at the same time.
 So a class can get features from multiple sources. Like a child who inherits cooking skills from mom 
 and business skills from dad.

7. Polymorphism

Poly means many, morph means forms. Same method name but different behavior in different classes. 
For example, both a Dog and a Cat have a speak() method — Dog says "Woof" and Cat says "Meow." Same name, 
different output.

8. Method Overriding
When a child class redefines a method that already exists in the parent class, 
it is called method overriding. The child's version will be used instead of the parent's. It's like a company 
rule being overridden by a local office rule.

9. Abstraction
Abstraction means showing only what is necessary and hiding the complex background details. 
Like a TV remote — you press a button and it works, you don't need to know the circuit inside. 
In Python, abstract classes force child classes to implement certain methods.

10. super()

super() is used to call the parent class's method or constructor from inside the child class. 
It avoids rewriting parent code and ensures the parent is properly initialized before the child adds its own stuff.

11. Class Variable vs Instance Variable

A class variable is shared by all objects of the class — like a school name shared by all students.
 An instance variable is unique to each object — like each student's own roll number.

12. @classmethod

A class method is bound to the class itself, not to any specific object. It can access and modify class-level data.
 It receives cls (the class) as its first argument instead of self.

13. @staticmethod
A static method doesn't depend on the class or object at all. It's just a regular function placed inside a 
class for organizational purposes. It doesn't receive self or cls.

14. Magic / Dunder Methods

These are special built-in methods surrounded by double underscores like __str__, __len__, __repr__.
 They define how objects behave with built-in Python operations. For example, __str__ defines 
 what gets printed when you print an object.

15. Operator Overloading

By default, operators like +, -, == work on numbers and strings. But using dunder 
methods, you can define what these operators do on your custom objects. For example, you can 
define __add__ to make two "Bag" objects combine their items when you use +.



# One-Line Summary of All

=================================================================================================================================================================
    Concept.              ||              Simple Meaning
=================================================================================================================================================================
1. Class & Object                     Blueprint & real thing
==================================================================================================================================================================
2. __init__                           Auto-setup when object is created
==================================================================================================================================================================
3. self                               Refers to the current object
===================================================================================================================================================================
4. Encapsulation                      Hide & protect data
===================================================================================================================================================================
5. Inheritance                        Child gets parent's features
===================================================================================================================================================================
6. Multiple Inheritance               Inherit from many parents
===================================================================================================================================================================
7. Polymorphism                       Same name, different behavior
===================================================================================================================================================================
8. Method Overriding                  Child rewrites parent's method
===================================================================================================================================================================
9. Abstraction                        Show only what's needed
===================================================================================================================================================================
10. super()                           Access parent from child
====================================================================================================================================================================
11. Class vs Instance Variable        Shared vs personal data
====================================================================================================================================================================
12. @classmethod                      Works on class level
====================================================================================================================================================================
13. @staticmethod                     Independent utility method
====================================================================================================================================================================
14. Dunder Methods                    Special behavior methods
====================================================================================================================================================================
15.Operator Overloading               Custom behavior for operators
====================================================================================================================================================================
'''
#===================================================================================================================================================================

''' CLASS AND OBJECT IN PYTHON 
 class is a BLUEPRINT for creating objects.'''

#creating class 

class Student:
   name = "karan aujla"

#Creating objects (instance)

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

# one more example 

class Car:
   color = "blue"
   brand = "bmw"
car1 = Car()
print(car1.color)

#===========================================================================================================================================================================

''' __init__ function

all classes have a function called __init_(), which is always executed when the class is being initiated. '''

# creating class 

class Student:
   def __init__(self, fullname):
      self.name = fullname

# creating objects 

s1 = Student("karan")
print(s1.name)

'''The self parameter is a reference to the current instance of the class, and is used to access variables
that belong to the class '''

class Student :
   def __init__(self,fullname,marks):
      self.name = fullname
      self.marks = marks
      print("adding a new student in database..")

s1 = Student("karan",88)
print(s1.name)

s2 = Student("anushka",97)
print(s2.name)

#================================================================================================================================================================

''' CLASS AND INSTANCE ATTRIBUTES

attributes = data(variable) 
  
class.attr 
obj.attr

  '''

class Student:
   college_name = "abc college"
   name = "anonymous"

   def __init__(self,name,marks):
      self.name = name #obj attr > class class attr 
      self.marks = marks 
      print("adding new students in Database..")

s1 = Student("karan",97)
      
#================================================================================================================================================================

'''  METHODS 
methods are function that belong to objects.
'''

class Student:
   college_name = "abc college"

   def __init__(self,name,marks):
      self.name = name #obj attr > class class attr 
      self.marks = marks 
      print("adding new students in Database..")

   def welcome(self):
      print("welcome students,", self.name)

   def get_marks(self):
      return self.marks 

s1 = Student("karan",97)
s1.welcome()
print(s1.get_marks())

#==================================================================================================================================================
'''
STATIC METHODS
method that don't use the self parameter (work at class level)

class Student:
   @staticmethod #decorator
   def college():
       print("abc college")


* decorators allows us to wrap another function in order to extend the behavior of the wrapped function,
 without permanently modifying it

'''
class Student:
   college_name = "abc college"

   def __init__(self,name,marks):
      self.name = name #obj attr > class class attr 
      self.marks = marks 
      print("adding new students in Database..")

   @staticmethod # working of @staticmethod(function)
   def hello():
      print("hello")

   def welcome(self):
      print("welcome students,", self.name)

   def get_marks(self):
      return self.marks 

s1 = Student("karan",97)
s1.welcome()
print(s1.get_marks())

#=======================================================================================================================

'''.      IMPORTANT      

1. ABSTRACTION

hiding the implementation details of a class and only showing the essential features to the user. 

2. ENCAPSULATION 

Wrapping data and function into a single unit (object).

'''

# (A) ABSTRACTION ( TO HIDE UNNECESSARY THIS )

class Car:
   def __init__(self):
      self.acc = False
      self.brk = False
      self.clutch = False

   def start(self):
      self.clutch = True
      self.acc = True

car1 = Car()
car1.start() 

# (B) ENCAPSULATION  ( DATA+FUNCTION = CAPSULE)

class Dog:
    def __init__(self, name):
        self.__name = name        # Private

    def get_name(self):
        return self.__name        # Public method to access it

dog = Dog("Bruno")
print(dog.get_name())             # Bruno
# print(dog.__name)               # Error!


















