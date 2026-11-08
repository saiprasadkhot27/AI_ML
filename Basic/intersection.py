arr1 = [10, 20, 30, 40, 50]
arr2 = [30, 40, 50, 60, 70]

result = []

for i in arr1:
    if i in arr2:
        result.append(i)

print("Common elements:", result)