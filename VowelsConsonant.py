string = input("Enter String : ")

vowel_count = 0
consonant_count = 0

vowels = "aeiouAEIOU"

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1   

print(f"Vowels = {vowel_count} ")  
print(f"Consonant = {consonant_count}")      