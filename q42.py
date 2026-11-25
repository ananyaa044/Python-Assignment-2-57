# 42. Print an increasing number pattern using nested loops.
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end="")
    print()
