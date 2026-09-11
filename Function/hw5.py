def remove(orig, x, out):
    num = 0
    for i in range(10):
        if orig[i] != x:
            out[num] = orig[i]
            num += 1
        else:
            continue
    return out


orig = list(map(int, input("Enter a list of ten integers: ").split()))
x = int(input("Enter an integer to remove: "))
out = [0] * 10
a = input("Enter a list of another ten integers: ")
print(remove(orig, x, out))