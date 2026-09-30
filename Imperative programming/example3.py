n = int(input("Enter a positive integer: "))
# FIX: before, if the first input was not positive, the program asked again but never calculated n!.
# Also the task asks for a while-loop (Example 4 is the for-version).
if n <= 0:
    print("Input error: n must be a positive integer.")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"The factorial of {n} is {factorial}")
