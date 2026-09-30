def read_floats(n):
    lst = []
    for i in range(n):
        # FIX: the task wants the prompt 'input value 1 out of 6:'
        lst.append(float(input(f'input value {i + 1} out of {n}: ')))
    return lst

n = int(input("Enter a nonnegative integer: "))
print(read_floats(n))