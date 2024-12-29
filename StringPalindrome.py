string = input("Enter String : ")

string = string.lower()

if string == string[::1]:
    print(f"The String {string} Is Palindrome.")
else:
    print(f"The String {string} Is Not Palindrome.")    