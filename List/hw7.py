a = 0
lst = []
while a >= 0:
    a = int(input("Enter a nonnegative integer: "))
    if a < 0:
        break
    if a in lst:
        lst.remove(a)
        lst.insert(0, a)
    else:
        lst.insert(0, a)

print(lst)