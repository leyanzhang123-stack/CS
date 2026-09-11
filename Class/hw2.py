def birthday_id(ssn):
    lst = []
    if ssn[6] == '+':
        lst.append('18')
    elif ssn[6] == '-':
        lst.append('19')
    else:
        lst.append('20')
    lst[0] = int(lst[0] + ssn[4:6])

    if int(ssn[2:4]) < 10:
        lst.append(int(ssn[2:4]))
    else:
        lst.append(int(ssn[3:4]))

    lst.append(int(ssn[:2]))

    return lst

ssn = input("Enter a social security number (YYMMDD-XXXX): ")
print(f'({birthday_id(ssn)[0]}, {birthday_id(ssn)[1]}, {birthday_id(ssn)[2]})')