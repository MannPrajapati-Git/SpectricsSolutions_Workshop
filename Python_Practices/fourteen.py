# 14. Store 5 characters in a list. Count how many are vowels and how many are consonants.

character = ["a", "b", "c", "d", "e"]
vowels = 0
consonants = 0
for i in character:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
print("vowels:", vowels)
print("consonants:", consonants)