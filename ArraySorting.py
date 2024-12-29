def ArraySort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array:", arr)


num = int(input("Enter number of elements: "))
arr = []


for i in range(num):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)


print("Array:", arr)

ArraySort(arr)

arr.sort(reverse=True)

print("Array after Desc : ",arr)


