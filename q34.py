# 34. Calculate the factorial of a number using a loop.
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print("Factorial of", number, "is", factorial)
