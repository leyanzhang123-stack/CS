def file_type(s):
    # FIX: s.index('.') finds the FIRST dot, so 'foo.bar.docx' gave 'bar.docx'.
    # rfind finds the LAST dot and returns -1 if there is none.
    i = s.rfind('.')
    if i == -1:
        return ''
    return s[i + 1:]

s = input("Enter a file name: ")
print(file_type(s))
