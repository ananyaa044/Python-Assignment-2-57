# 16. Demonstrate left-shift and right-shift operators.
number = int(input("Enter an integer: "))
places = int(input("Enter the number of bit positions to shift: "))

if places < 0:
    print("The number of positions must not be negative.")
else:
    print("Left shift =", number << places)
    print("Right shift =", number >> places)
