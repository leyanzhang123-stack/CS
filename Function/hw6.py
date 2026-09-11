def alternate(lst):
    new = []
    for i in range(len(lst) // 2):
        new.append(lst[i])
        new.append(lst[len(lst) - 1 - i])
    if len(lst) % 2 != 0:
        new.append(lst[len(lst) // 2])
    return new

lst = list(map(int, input("Enter a list of integers: ").split()))
print(alternate(lst))