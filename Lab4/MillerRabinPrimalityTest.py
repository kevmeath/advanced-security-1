import random


def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1:
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result


def miller_rabin(d, n):
    a = 2 + random.randint(1, n - 4)

    x = power(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not miller_rabin(d, n):
            return False

    return True


k = 4

print("1. Test one number\n"
      "2. Test a range of numbers")
option = input("Select an option: ")
if option == '1':
    n = int(input("Enter a number to test: "))
    if is_prime(n, k):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
elif option == '2':
    a = int(input("Enter range start: "))
    b = int(input("Enter range end: "))
    print(f"Prime numbers between {a} and {b}:")
    for n in range(a, b):
        if is_prime(n, k):
            print(f"{n}")
else:
    print("Invalid input")
