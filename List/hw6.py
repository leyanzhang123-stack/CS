import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
lst = []
print(list_of_lists)
for i in range(5):
    for j in range(n):
        # FIX: flattening keeps ALL elements (50 of them), including repeats.
        # Before, "if not (a in lst)" removed duplicates, so the result had only 10 elements.
        lst.append(list_of_lists[i][j])
print(lst)
