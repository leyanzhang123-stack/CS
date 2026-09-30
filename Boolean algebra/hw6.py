n = int(input("Enter a positive integer: "))
a = True

if n < 2:  # FIX: 0 and 1 are not primes (before, 1 was reported as prime), and the program now stops here
    print(f"{n} is not a prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            a = False
            break

    if a == True:
        print(f"{n} is a prime number.")
