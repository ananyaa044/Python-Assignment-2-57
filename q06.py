# 6. Demonstrate the difference between / and // operators.
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if second == 0:
    print("The second integer must not be zero.")
else:
    print("/ (true division) =", first / second)
    print("// (floor division) =", first // second)
