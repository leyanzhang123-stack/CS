s = int(input("Enter a positive integer: "))
if s < 0:
    print("Please enter a positive integer only.")
n = 10
while True:
    if n ** 3 * (n - 10) > s:
        print(f"The smallest integer n such that n^3 * (n - 10) > {s} is {n}.")
        break
    n += 1
