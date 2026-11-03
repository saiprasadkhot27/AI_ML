# def outer():
#     print("Outer is called")

#     def inner():
#         print("Inner is called")
#         return None
#     return inner()
# print(outer())

# def outer():
#     print("Outer is called")

#     def inner():
#         print("Inner is called")
#         return "Hi"
        
#     return inner
# # print(outer())

# something=outer()
# # print(something)
# something()


def greet():
    def message():
        print("Welcome to python")
    return message
something=greet()
something()
        