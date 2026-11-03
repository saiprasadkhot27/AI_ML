# class demo:
#     print("Demo")
# r=demo()

# print(r)
# print(type(r))


# class computer:
#     def config(self):
#         print("i5 512 GB 16 GB")
# o1=computer()
# o2=computer()

# computer.config(o1)
# computer.config(o2)
# o1.config()
# o2.config

# class laptop:
#     def details(self,brand,ram):
#         print(brand)
#         print(ram)
# l1=laptop()
# l2=laptop()
# l1.details("hp",13)
# l2.details("dell",14)



#init method

# class computer:
#     def __init__(self):
#         self.cpu="i5"
#         self.ram="16GB"
#         self.brand="Dell"
#     def config(self):
#         print("CPU :",self.cpu)
#         print("Brand:",self.brand)
#         print("ram:",self.ram)

    
# d1=computer()
# d1.config()


# with argument

class computer:
    def __init__(self,cpu,brand,ram):
        self.cpu=cpu
        self.ram=ram
        self.brand=brand
    def config(self):
        print("CPU :",self.cpu)
        print("Brand:",self.brand)
        print("ram:",self.ram)

    
d1=computer("i5","HP","32GB")
d1.config()

