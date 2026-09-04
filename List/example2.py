a = 0
lst = []
while a >= 0:
    a = int(input("Please enter a nonnegative number: ")) 
    if a >= 0:
        lst.append(a)
    lst.sort()
print(lst)
