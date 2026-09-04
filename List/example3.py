a = ''
lst = []
while len(a) < 4:
    a = input("Please enter something: ")
    if len(a) < 4:
        lst.append(a)
print(lst)