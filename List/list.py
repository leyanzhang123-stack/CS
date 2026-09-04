'''import random
lst = [1, 8, 3, 4, 5, 6, 7, 8, 9, 10]
lst.sort()
print(lst)
a = random.sample(lst,3)
print(a)'''

lst = [x for x in range(10) if x % 3 == 0]
print(lst)