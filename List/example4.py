import random
n = 12
lst = random.sample(list(range(n)), n)
diff = []

for i in range(n - 1): diff.append(lst[i + 1] - lst[i])

print(f'list: {lst}')
print(f'diff: {diff}')

# FIX: the task asks for a one-line version using a list comprehension, slices and zip():
print([b - a for (a, b) in zip(lst, lst[1:])])