b = True
i = 1  # FIX: n must be a positive integer, so start at 1
while b:
    if (i ** 3 - 16) % 47 == 0:
        print(f"{i} ** 3 - 16 is divisible by 47")
        b = False
    else: 
        i += 1