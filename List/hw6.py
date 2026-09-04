import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
lst = []
print(list_of_lists)
for i in range(5):
    for j in range(n):
        a = list_of_lists[i][j]
        if not(a in lst):
            lst.append(a)
print(lst)
