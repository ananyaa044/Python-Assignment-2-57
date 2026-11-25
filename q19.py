# 19. Demonstrate the identity operators is and is not.
first = [1, 2, 3]
second = first
third = [1, 2, 3]

print("first is second:", first is second)  # True: both names refer to the same object
print("first is third:", first is third)  # False: these are separate objects
print("first is not third:", first is not third)