import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
lst = []
for i in range(5):
    for j in range(n):
        a = list_of_lists[i][j]
        if not(a in lst):
            lst.append(a)
print(lst)
print("Half way done")
'''for i in range(len(lst)):
    for j in range(5):
        if lst[i] in list_of_lists[j]:
            list_of_lists[j].remove(lst[i])
print(list_of_lists)'''
