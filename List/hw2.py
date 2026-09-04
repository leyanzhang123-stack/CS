a = 14
pos = []
neg = []
while a != 0:
    a = int(input("Please enter a number: "))
    if a > 0:
        pos.append(a)
    elif a < 0:
        neg.append(a)
print(pos)
print(neg)