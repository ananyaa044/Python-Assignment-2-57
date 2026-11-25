# 46. Print numbers from 1 to 20, skipping multiples of 3 with continue.
for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)
