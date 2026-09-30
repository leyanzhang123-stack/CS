def last_dot_kept(s):
    # FIX: the task is to replace every dot EXCEPT the last one.
    # Before, the code replaced only the last dot, and with no dots at all it replaced s[0].
    total = s.count('.')
    count = 0
    result = []
    for c in s:
        if c == '.':
            count += 1
            if count < total:
                result.append('-dot-')
            else:
                result.append('.')   # the last dot is kept
        else:
            result.append(c)
    return ''.join(result)

s = input("Enter a string with dots: ")
print(last_dot_kept(s))
