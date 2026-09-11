def f(x):
    return 0.5 * (x + 2 / x)

def interate(f, x, n):
    lst = []
    for i in range(n):
        x = f(x)
        lst.append(x)
    return lst

x = int(input("Enter an integer: "))
n = int(input("Enter the number of iterations: "))
print(interate(f, x, n))