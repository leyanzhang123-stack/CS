def fun(x):
    flag = True 
    i = 2
    while flag and i < len(x):
        if x[i] - x[i-1] != x[i-1] - x[i-2]:
            flag = False
        else:
            i += 1
    return flag  # FIX: the given function returns only flag

x = [int(i) for i in input("Please give a list of integers separated by spaces: ").split()]
print(fun(x))

#purpose: to check if a list of integers forms an arithmetic progression