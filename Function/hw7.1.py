def f(x):
    return 0.5 * (x + 2 / x)

def iterate(f, x, n):  # FIX: name was interate
    lst = []
    for i in range(n):
        x = f(x)
        lst.append(x)
    return lst

# FIX: the task says call it with x = 1 and n = 6 (the values approach sqrt(2))
print(iterate(f, 1, 6))