# 8. Swap two numbers using arithmetic operators.
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print("Before swapping:", first, second)
first = first + second
second = first - second
first = first - second

print("After swapping:", first, second)
