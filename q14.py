# 14. Check whether a number is divisible by both 3 and 5 using logical operators.
number = int(input("Enter an integer: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
