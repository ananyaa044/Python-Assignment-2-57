# 28. Check whether a character is a vowel or consonant.
character = input("Enter a single alphabet character: ").lower()

if len(character) != 1 or not character.isalpha():
    print("Please enter exactly one alphabet character.")
elif character in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
