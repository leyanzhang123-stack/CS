# FIX: before, "while True" never ended, and print was written three times.
# "Avoid duplication": store the action in a variable and print it once.
total = int(input("Enter the total: "))
if total < 17:
    action = "hit"
elif total <= 21:
    action = "stay"
else:
    action = "bust"
print(action)
