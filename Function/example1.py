def abs_value(x):
    if x < 0:
        return -x
    else:
        return x

def distance(a, b):
    return abs_value(a - b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
d = distance(a, b)
print("The distance between", a, "and", b, "is", d)