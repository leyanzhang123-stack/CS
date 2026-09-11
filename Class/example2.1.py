def last_dot_kept(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '.':
            count += 1
        if count == s.count('.'):
            s = s[:i] + '-dot-' + s[i+1:]
            break
    return s

s = input("Enter a string with dots: ")
print(last_dot_kept(s))