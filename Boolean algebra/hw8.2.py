a = True
n = 2
print(2, end =" ")
t = 1
while t < 100:
    n += 1
    a = True
    for i in range(2, n):
        if n % i == 0:
            a = False
            break
        else:
            continue
    if a == True:
        print(n, end =" ")
        t += 1
    