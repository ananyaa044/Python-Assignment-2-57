# 36. Reverse a given integer using a while loop.
number = int(input("Enter an integer: "))
sign = -1 if number < 0 else 1
remaining = abs(number)
reversed_number = 0

while remaining > 0:
    digit = remaining % 10
    reversed_number = reversed_number * 10 + digit
    remaining //= 10

print("Reversed integer:", sign * reversed_number)
