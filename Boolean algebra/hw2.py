a = int(input("Enter a positive integer: "))
b = int(input("Enter a positive integer: "))
if a <= 0 or b <= 0:  # FIX: 0 is not positive
    print("Please enter positive integers only.")
elif a % 10 == b % 10:
    print("True")
else:
    print("False")