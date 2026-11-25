# 20. Evaluate expressions to demonstrate Python operator precedence.
a = 10
b = 5
c = 2

print("10 + 5 * 2 =", a + b * c)  # Multiplication happens first: 20
print("(10 + 5) * 2 =", (a + b) * c)  # Parentheses happen first: 30
print("10 - 5 ** 2 =", a - b ** c)  # Exponentiation happens first: -15
print("10 / 5 + 2 =", a / b + c)  # Division happens before addition: 4.0
