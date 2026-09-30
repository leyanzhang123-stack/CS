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

# FIX: this exercise only asks for a trace, not a purpose.
# For N=139 and L=3 the output is: 3 True   (d: 46 -> 15 -> 5, z: 1 -> 2 -> 3, b: F -> T -> F)