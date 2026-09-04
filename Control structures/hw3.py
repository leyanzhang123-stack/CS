N = int(input("Please give a number N: "))
L = int(input("Please give a number L: "))

d = N // L
z = 1
b = False

while z < L:
    d = d // L
    z += 1
    b = not b

if d != 0 and b:
    print(d, b)
else:
    print(z, not b)

#purpose: to find the largest power of L that divides N