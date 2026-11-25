#3. Write a program to calculate the remainder without using the modulus operator.
a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
remainder = a - (a // b) * b
print("The remainder of", a, "divided by", b, "is:", remainder)
