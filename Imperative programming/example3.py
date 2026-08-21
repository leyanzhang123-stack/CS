n = int(input("Enter a positive integer: "))
if n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")
while n <= 0:
    print("Please enter a positive integer.")
    n = int(input("Enter a positive integer: "))