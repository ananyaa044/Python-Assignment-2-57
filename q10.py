# 10. Calculate the sum of the digits of a two-digit number.
number = int(input("Enter a two-digit integer: "))

if 10 <= abs(number) <= 99:
    tens_digit = abs(number) // 10
    ones_digit = abs(number) % 10
    print("Sum of digits =", tens_digit + ones_digit)
else:
    print("Please enter a two-digit integer.")
