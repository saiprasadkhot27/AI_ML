# import sys

# def greet():
#     print("Hello Students")
#     greet()
# greet()


def factorial(num):
    if num==1:
        return 1
    
    return num*factorial(num-1)
f=factorial(5)
print(f)
