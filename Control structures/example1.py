a = int(input("please give a: "))
b = int(input("please give b: "))
c = int(input("please give c: "))
ab = a - b
bc = b - c
ac = a - c

if ab * bc > 0:
    result = b
elif ab * ac < 0:  # FIX: the pseudocode says AB * AC < 0 (with > 0, e.g. 2, 1, 3 gave 3 instead of 2)
    result = a
else:
    result = c

print(result)

#purpose: to find the middle number of three numbers