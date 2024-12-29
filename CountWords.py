string = input("Enter String : ")

word = 0
in_word = False

for char in string:
    if char != ' ' and not in_word:
        word+=1
        in_word=True
    elif char == ' ':
        in_word=False

print(f"Words in the string : ",word)            