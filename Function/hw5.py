def remove(orig, x, out):
    num = 0
    for i in range(10):
        if orig[i] != x:
            out[num] = orig[i]
            num += 1
    # FIX: the rest of OUT must be zeros. Before, it only worked because out started as [0] * 10;
    # with OUT = [6, 6, ..., 6] (the handout example) the end stayed 6.
    for i in range(num, 10):
        out[i] = 0
    return out


orig = list(map(int, input("Enter a list of ten integers: ").split()))
x = int(input("Enter an integer to remove: "))
out = [6] * 10  # FIX: removed an input that was never used; OUT is the handout's example
print(remove(orig, x, out))