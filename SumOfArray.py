# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# sum = arr1+arr2

# print(sum)


def ArraySum(arr1,arr2):
    if len(arr1)!=len(arr2):
        print("Array must have same length")
        return None
    
    sum = []

    for i in range(len(arr1)):
        sum.append(arr1[i]+arr2[i])

    print("Sum of two array", sum) 

num = int(input("Enter number of elements"))
arr1 = [] 
arr2 = []

for i in range(num):
    element = int(input(f"Enter First Array Element {i+1} : "))
    arr1.append(element)

print("First Array : ",arr1)


for i in range(num):
    element = int(input(f"Enter Second Array Element {i+1} : "))
    arr2.append(element)

print("Second Array : ",arr2)



ArraySum(arr1,arr2)