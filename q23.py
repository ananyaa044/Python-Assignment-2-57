# 23. Find the greatest among two numbers.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print("The greatest number is", a)
elif b > a:
    print("The greatest number is", b)
else:
    print("Both numbers are equal.")
