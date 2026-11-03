# class abc:
#     def __new__(cls):
#         print("constructor is called")
#         return super().__new__(cls)
#     def __init__(self):
#         print("Init is called...")
    
    
# d1=abc()




class sample:
    def __new__(cls):
        print("New is called")
        return super().__new__(cls)
    def __init__(self):
        print("Init is called")

    def method(self):
        print("Method is called")

d1=sample()
d1.method()