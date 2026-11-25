# 40. Print all prime numbers within a given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start > end:
    print("The start of the range must not exceed the end.")
else:
    print("Prime numbers:")
    for number in range(max(2, start), end + 1):
        is_prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print(number)
