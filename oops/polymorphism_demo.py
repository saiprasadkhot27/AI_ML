
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Object creation
a1 = Animal()
d1 = Dog()
c1 = Cat()

# Calling methods
a1.sound()
d1.sound()
c1.sound()
