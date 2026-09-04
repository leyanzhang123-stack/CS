a = int(input("please give a: "))
b = int(input("please give b: "))
c = int(input("please give c: "))
ab = a - b
bc = b - c
ac = a - c

if ab * bc > 0:
    result = b
elif ab * ac > 0:
    result = a
else:
    result = c

print(result)

#purpose: to find the middle number of three numbers