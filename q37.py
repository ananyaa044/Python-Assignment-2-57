# 37. Count the number of digits in a given integer.
number = int(input("Enter an integer: "))
remaining = abs(number)
count = 1 if remaining == 0 else 0

while remaining > 0:
    count += 1
    remaining //= 10

print("Number of digits:", count)
