# 17. Check whether a number is even or odd using a bitwise operator.
number = int(input("Enter an integer: "))

if number & 1:
    print("Odd")
else:
    print("Even")
