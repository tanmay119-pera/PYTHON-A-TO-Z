'''                                        PRACTICE OOPS                                                          '''
'''
problem no.1 

Define a circle class to create a circle with radius 'r' using the constructor. Define an area() method of the class
which calculates the area of the circle. define a perimeter() method of the class which allows you to calculate 
the perimeter of the circle.
'''

# removed unused import


class Circle:
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return 22/7 * self.radius ** 2      # we can even take pie = 3.14 for more accurate answer.
    
    def perimeter(self):
        return 2 * 22/7 * self.radius


c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


'''

problem no.2

define employee class with attribute role, department and salary this class also showDetails() method. Create a 
engineer class that inherits the properties of employee and has additional attributes : name:age  

'''
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept 
        self.salary = salary 

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role="Engineer", dept="IT", salary=75000):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        super().showDetails()
        print("Name=", self.name)
        print("Age=", self.age)

e1 = Employee("Manager", "HR", 50000)
e1.showDetails()

eng = Engineer("Alice", 30)
eng.showDetails()

'''

problem no.3

create a class called order which stores item and price use dunder function __gt__() to convey that :
order 1 > order 2 if price of order 1 > price of order:

'''

class Order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price  
    
ord1 = Order("chips", 20)
ord2 = Order("tea", 15)

print(ord1 > ord2) # true







