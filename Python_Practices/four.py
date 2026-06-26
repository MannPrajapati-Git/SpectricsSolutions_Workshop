# 4. Take a single character (str) as input. Check whether it is a vowel, consonant, or digit.

character = input("Enter a character: ")
vowel = ['a','e','i','o','u','A','E','I','O','U']

if character in vowel:
    print("Vowel")
elif character.isalpha():
    print("Consonant")
else:
    print("Digit")