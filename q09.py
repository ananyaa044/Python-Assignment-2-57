# 9. Calculate the last digit of an integer using arithmetic operators.
number = int(input("Enter an integer: "))

last_digit = abs(number) % 10
print("Last digit =", last_digit)
