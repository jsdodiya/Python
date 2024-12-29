# arr = [3,4,5,7,423,45,56,2,3,52,24,56,672,442,11,244,99,654]
# arr.sort()

# print("Sorted Array : ",arr)
# print("Second Largest Number : ",arr[-2])


arr1 = []
 
for i  in range(0,5):
    E = int(input(f"Enter Array Element {i+1} : "))
    arr1.append(E)

arr1.sort()
print("Array : ",arr1)

largest = second = float('-inf')

for i in arr1:
    if i>largest:
        second = largest
        largest = i
    elif i>second and i!=largest:
        second = i 

print("Second Largest Element : ",second)           
 