# 43. Print multiplication tables from 1 to 10 using nested loops.
for number in range(1, 11):
    print(f"Table of {number}:")
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")
    print()
