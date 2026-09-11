def apply_functions(fs, x):
    j = reversed(fs)
    for i in j:
        x = i(x)
    return x

b = ['...'.join, str.split, str.lower]
m = "WHAT IS THIS?"
print(apply_functions(b, m))
    