s = input("Enter a string:")  # FIX: s was never defined, so this file crashed
max = 1
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        if count > max:
            max = count
        count = 1
if count > max: max = count
if s == '': max = 0  # FIX: empty string gives 0
print(max)
