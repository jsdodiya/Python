def MaxMin(arr):
    max = arr[0]
    min = arr[0]

    for num in arr:
        if num>max:
            max=num
        if num<min:
            min=num
    print(f"Maximum Element = {max} and Minimum Element = {min}")

n = int(input("Enter Number Of Elements"))
arr = []

for i in range(n):
    E = int(input(f"Enter Element Of Array {i+1} : "))
    arr.append(E)

print("Array : ",arr )

MaxMin(arr)