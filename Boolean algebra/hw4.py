a = int(input("Enter a positive integer: "))
b = int(input("Enter a positive integer: "))
if a < 0 or b < 0:
    print("Please enter positive integers only.")
m = 1
n = 1
while True:
    if a * m == b * n:
        print(f"The smallest positive integer that is divisible by {a} and {b} is {a * m}.")
        break
    else:
        if a * m < b * n:
            m += 1
        else:
            n += 1