def read_floats(n):
    lst = []
    for i in range(n):
        lst.append(float(input("Enter a float: ")))
    return lst

n = int(input("Enter a nonnegative integer: "))
print(read_floats(n))