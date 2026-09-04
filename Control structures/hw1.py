result = int(input("Please give an integer A: "))
b = int(input("Please give an integer B: "))
c = int(input("Please give an integer C: "))

if b > result:
    result = b
if c > result:
    result = c

print(result)

#purpose: to find the maximum of three numbers