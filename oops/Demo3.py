class Employee:
    def __init__(self, name):
        self.name = name
        print("Created:", self.name)

    def display(self):
        print("Employee:", self.name)

    def __del__(self):
        print("Destroyed:", self.name)


e1 = Employee("Rahul")
e2 = Employee("Amit")

e1.display()
e2.display()

del e1
del e2