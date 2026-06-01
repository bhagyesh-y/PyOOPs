# This is inheritance 
# Inheritance is the process of inheriting the properties of the parent class to the child class
# Example: Person class has a name and age attribute, Employee class has a name and age attribute, Employee class has a salary attribute
# Person class is the parent class, Employee class is the child class
# Employee class inherits the properties of the Person class
# Employee class can access the properties of the Person class
# Employee class can access the methods of the Person class
# Employee class can access the instance variables of the Person class
# Employee class can access the class variables of the Person class
# Employee class can access the static methods of the Person class
print("Inheritance")

class P:
    def m1(self):
        print("parent class method") 
class C(P):
    def m2(self):
        print("child class method")
c = C()
# here child class method is called by the parent class method
c.m1()
c.m2()  
# here parent class method is called by the child class method

print("demo 1 is ended , 2nd demo is started")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age # here age is a instance variable of the parent class
    def eatdrink(self):
        print("Eat Biryani and drink coldrink")   
class Employee(Person):
    def __init__(self, name, age,eno,esal):
        super().__init__(name,age) # here name and age are instance variables of the parent class   
        self.eno=eno
        self.esal=esal
    def work(work): # here work is a method of the child class
        print("Coding in python is quite interesting") 
    def empinfo(self):
        print("Employee Name:",self.name)   # here name is a instance variable of the parent class
        print("Employee Age:",self.age) # here age is a instance variable of the parent class
        print("Employee Number:",self.eno) # here eno is a instance variable of the child class
        print("Employee Salary:",self.esal) # here esal is a instance variable of the child class                 
e=Employee("Bhagyesh",25,12,120000) 
e.eatdrink() # here eatdrink is a method of the parent class
e.work() # here work is a method of the child class 
e.empinfo()

        