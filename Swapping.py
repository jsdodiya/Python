# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter first number : "))

# print(f"Before swap num1 ={num1} and num2 = {num2}")
# temp = num1
# num1 = num2
# num2 = temp

# print(f"After swap num1 = {num1} and num2 = {num2}")


num1 = int(input("Enter first number : "))
num2 = int(input("Enter first number : "))

print(f"Before swap num1 ={num1} and num2 = {num2}")

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print(f"After swap num1 = {num1} and num2 = {num2}")