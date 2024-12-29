def addArray(arr1,arr2):
    arr3 = arr1+arr2
    print("New Array After Adding Elements Of Both Array",arr3)    

    n = len(arr3)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr3[j] > arr3[j+1] :
             arr3[j],arr3[j+1] = arr3[j+1],arr3[j]
    print("Array After Sorting : ",arr3)
    # print("Second Largest Number in Array",arr3[-2])            

    
    arr3.sort(reverse=True)
    print("Array After Reverse",arr3)


n = int(input("Enter elemtents of array"))

arr1= []

for i in range(n):
    element = int(input(f"Enter First Array Element {i+1} :"))
    arr1.append(element)

print("First Array Elements: ",arr1)

arr2 = []

for i in range(n):
    element=int(input(f"Enter Second Array Element {i+1} : "))
    arr2.append(element)

print("Second Array Element : ",arr2)

addArray(arr1,arr2)