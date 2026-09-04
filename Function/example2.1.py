def interleave(a, b):
    if len(a) != len(b):
        return "Error: Lists must be of the same length."
    else:
        lst = []
        l = 0
        while l < len(a):
            for i in range(2):
                if i == 0:
                    lst.append(a[l])
                else:
                    lst.append(b[l])
            l += 1
        return lst

a = list(map(int, input("enter a list: ").split()))
b = list(map(int, input("enter another list: ").split()))
print(interleave(a, b))