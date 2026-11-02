from functools import reduce
# nums=[1,2,3,4,5,6,7,8,9,10,11,12]

# is_even=lambda num:True if num%2==0 else False

# r=list(filter(is_even,nums))
# print(r)
# def is_add(a,b):
#     return a+b

# n=[34,56,35,676,3645,12,342,63]
# r=list(filter(lambda n:True if n>50 else False,n))
# r2=list(map(lambda n:n*2,n))
# print(reduce(is_add,r2))

# print(r)
# print(r2)


print(reduce(lambda a,b:a+b,list(map(lambda num:num*num*num,[1,2,3]))))
