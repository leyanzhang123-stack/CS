a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# FIX: the task says "use a variable to avoid duplication", so compute a + b once
s = a + b
if a == b:
    print(s ** 2)
else:
    print(s)
