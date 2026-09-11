def file_type(s):
    for i in reversed(s):
        if i == '.':
            return s[s.index(i) + 1:]
    return ''

s = input("Enter a file name: ")
print(file_type(s))

        