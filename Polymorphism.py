# This is polymorphism 
# Polymorphism is the ability to take many forms like a same method name but different parameters
# Example: Animal class has a sound method, Dog class has a sound method, Cat class has a sound method


print("Polymorphism")

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

