def enter_list(n, k):
    lst = []
    for i in range(n):
        row = []                                        # create a new empty row
        for j in range(k):
            row.append(int(input("Enter an integer: ")))  # fill it
        lst.append(row)                                 # add the finished row to lst
    return lst

def transpose(lst):
    transposed = []
    for i in range(len(lst[0])):
        row = []
        for j in range(len(lst)):
            row.append(lst[j][i])
        transposed.append(row)
    return transposed

n = int(input("Enter the number of rows: "))
k = int(input("Enter the number of columns: "))
print(transpose(enter_list(n, k)))