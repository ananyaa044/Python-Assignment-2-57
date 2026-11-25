# 39. Check whether a number is prime using a loop.
number = int(input("Enter an integer: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
