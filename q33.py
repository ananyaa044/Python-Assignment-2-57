# 33. Calculate the sum of the first N natural numbers.
n = int(input("Enter a positive integer N: "))

if n < 1:
    print("N must be a positive integer.")
else:
    total = 0
    for number in range(1, n + 1):
        total += number
    print("Sum of the first", n, "natural numbers is", total)
