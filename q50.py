# 50. Print a decreasing star pattern using nested loops.
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end="")
    print()
