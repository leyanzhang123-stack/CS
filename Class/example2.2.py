def last_dot_kept(s):
    new = s.replace('.', '-dot-', count=s.count('.') - 1)
    return new

s = input("Enter a string with dots: ")
print(last_dot_kept(s))