#Function Overloading and Overriding 

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # Overriding
        print("Dog barks")

# Runtime behavior
a = Animal()
d = Dog()

a.sound()   # Calls Animal's method
d.sound()   # Calls Dog's overridden method

# Polymorphism
animal = Dog()
animal.sound()   # Calls Dog's method