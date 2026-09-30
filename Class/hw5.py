# FIX: the calculator must keep going until the user gives an empty input.
# Before, it ran only once, and an empty input crashed the unpacking.
while (line := input("my-calc: ")) != '':
    [a, op, b] = line.split()
    if op == '+':
        print(float(a) + float(b))
    elif op == '-':
        print(float(a) - float(b))
    elif op == '*':
        print(float(a) * float(b))
