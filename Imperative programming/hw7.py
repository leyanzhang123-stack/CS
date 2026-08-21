b = True
i = 0
while b:
    if (i ** 3 - 16) % 47 == 0:
        print(f"{i} ** 3 - 16 is divisible by 47")
        b = False
    else: 
        i += 1