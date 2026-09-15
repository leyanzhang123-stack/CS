max = 1
count = 1
s = 'abbbccdddd'
s = list(s.split())
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        print("yes!")
        count += 1
    else:
        if count > max:
            print("replace!")
            max = count
        count = 1
    print("next one!")