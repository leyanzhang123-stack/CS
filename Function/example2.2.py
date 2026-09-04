def interleave(a, b):
    flattened = []
    for (x, y) in zip(a, b):
        flattened.append(x)
        flattened.append(y)
    return flattened

a = list(map(int, input("enter a list: ").split()))
b = list(map(int, input("enter another list: ").split()))
if len(a) != len(b):
    print("Error: Lists must be of the same length.")
else:
    print(interleave(a, b))