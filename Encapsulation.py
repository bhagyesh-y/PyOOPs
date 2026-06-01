# This is encapsulation
# Encapsulation is the process of hiding the implementation details and showing only the functionality to the user
# Example: Student class has a name and age attribute, we can get the name and age of the student by using the getname and getage methods
print("Encapsulation")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.age

s=Student("Bhagyesh",25)
print(s.getname())