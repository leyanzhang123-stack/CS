n = int(input("How much does the package weigh? "))
if n <= 2:
    p = 3
elif n <= 5:
    p = 3 + (n - 2) * 2
else:
    p = 3 + 3 * 2 + (n - 5) * 3
print(f"This package will cost {p} euros to post.")