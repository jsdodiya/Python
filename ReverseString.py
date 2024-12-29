def ReverseString(string):
    reversed_string=""
    # for char in string:
    #     reversed_string = char + reversed_string
    reversed_string= string[::-1]
    print(f"Reversed String : ",reversed_string)    


string1 = input("Enter String : ")
print(f"Entered String : ",string1)

ReverseString(string1)