# FIX: the task asks for a function called date_of_birth(ssn) that returns a triple (y, m, d)
def date_of_birth(ssn):
    c = ssn[6]
    if c == '+':
        century = 1800
    elif c == '-':
        century = 1900
    else:
        century = 2000
    y = century + int(ssn[4:6])
    # FIX: before, months 10-12 used ssn[3:4], so December became 2. int('05') is already 5.
    m = int(ssn[2:4])
    d = int(ssn[0:2])
    return (y, m, d)

ssn = input("Enter a social security number (ddmmyycnnnh): ")
print(date_of_birth(ssn))   # FIX: call the function once, not three times
# test: date_of_birth('140598+abcd') should give (1898, 5, 14)
