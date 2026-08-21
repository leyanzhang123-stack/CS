bac1 = 0
bac2 = 0
max1 = 0
max2 = 0
t = 0
for i in range(1, 101):
    bac1 = i * (i - 20) * (i - 100) + 120000
    max1 = bac1 - bac2
    if max1 < max2:
        max2 = max1
        t = i
    bac2 = bac1
print(f"The maximum increase in the number of bacteria is {-max2} and it occurs at hour {t}.")