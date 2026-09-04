n = int(input("Enter a positive integer: "))
a = True

if n < 0:
    print("Please enter a positive integer only.")

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        a = False
        break
    else:
        continue
        
if a == True:
    print(f"{n} is a prime number.")
    