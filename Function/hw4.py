def share(a, b):
    for i in range(len(b)):
        if b[i] in a:
            return True
    return False

a = list(map(int, input("enter a list: ").split()))
b = list(map(int, input("enter another list: ").split()))
print(share(a, b))