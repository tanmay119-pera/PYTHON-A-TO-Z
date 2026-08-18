#problem no 1

'''
create students class that takes name and marks of 3 subjects as arguments in constructor 
then create a method to print the avg ''' 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):         
        total = 0               
        for val in self.marks:
            total += val        

        print("Hi", self.name, "your avg score is:", total / len(self.marks))
            
s1 = Student("tony stark",[99,98,97,69])
s1.get_avg() 

# problem no 2

'''
create account class with 2 attributes - balance and account no. create methods for debit and printing
the balance.

'''

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount          
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Total balance =", self.get_balance()) 

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 154659)
acc1.debit(1000)  
acc1.credit(5000)  