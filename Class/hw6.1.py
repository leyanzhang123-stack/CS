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
print(max)