import random
n = 12
lst = random.sample(a:= list(range(n)), n)
diff = []

for i in range(n - 1): diff.append(lst[i + 1] - lst[i])

print(f'list: {lst}')
print(f'diff: {diff}')