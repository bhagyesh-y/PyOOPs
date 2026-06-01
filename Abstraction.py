# This is abstraction, we can hide the implementation details and show only the functionality to the user
# Example: Animal class has a sound method, Dog class has a sound method, Cat class has a sound method
print("Abstraction")

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a=Animal()
a.sound()

d=Dog()
d.sound()

c=Cat()
c.sound()
