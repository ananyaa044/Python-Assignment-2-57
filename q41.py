# 41. Print a right-triangle star pattern using nested loops.
for row in range(1, 6):
    for column in range(row):
        print("*", end="")
    print()
