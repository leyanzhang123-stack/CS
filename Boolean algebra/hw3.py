s = int(input("Enter a positive integer: "))
if s <= 0:
    print("Please enter a positive integer only.")
else:  # FIX: before, the program kept running even after the error message
    n = 1  # FIX: start from the smallest positive integer, not 10
    while True:
        # FIX: the inequality is n^3 - 10n^2 > s. Before it said n ** 3 * (n - 10), which is n^4 - 10n^3
        if n ** 3 - 10 * n ** 2 > s:
            # FIX: the task also asks to print the value of the left hand side
            print(f"n = {n}, n^3 - 10n^2 = {n ** 3 - 10 * n ** 2}")
            break
        n += 1
