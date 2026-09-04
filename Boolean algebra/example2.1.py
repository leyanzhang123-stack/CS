n = int(input("Enter a year: "))
if (n % 400 == 0):
    print(f"{n} is a leap year." )
elif (n% 100 != 0 and n% 4 == 0):
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")