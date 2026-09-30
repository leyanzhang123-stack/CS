import random

# FIX: this file was unfinished ("x = random.uni").
# Count how many of 10000 random points (x, y) in ]-1, 1[ x ]-1, 1[ land inside the circle x^2 + y^2 <= 1.
t = 0
for i in range(10000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        t += 1
print(t / 10000)   # should be close to pi / 4 = 0.785..., i.e. 1 / (answer of hw10.1)
