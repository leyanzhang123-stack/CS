a = int(input("Enter a nonnegative integer: "))
num = 1
if a < 0:
    print("Error: negative number")
else:
    for i in range(a):
        num *= 3
print(num)