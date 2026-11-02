def  square(num):
    return num *num
def cube(num):
    return num*num*num
def operator(value,operation):
    # return operation(value)
    for num in value:
        r=operation(num)
        print(r)
# n=5
nums=[1,2,3]
print(operator(nums,square))
print(operator(nums,cube))
