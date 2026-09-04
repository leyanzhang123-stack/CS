a = True
print(2, end =" ")
for n in range (3, 101):
    a = True
    for i in range(2, n):
        if n % i == 0:
            a = False
            break
        else:
            continue
    if a == True:
        print(n, end =" ")