result = 1

x = int(input("Please give x: "))
y = int(input("Please give y: "))

while y > 0:
    if y % 2 == 0:
        y = y // 2  # FIX: 'div' is integer division; / turns y into a float
        x = x * x
    else:
        y = y - 1
        result = result * x

print(result)

#purpose: to calculate x^y using the method of exponentiation by squaring