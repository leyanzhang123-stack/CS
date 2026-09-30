# FIX: the task is: take a list of strings and REMOVE the strings whose length is at most 4.
# Before, the program read inputs until a long one and kept only the short ones.
words = ['cat', 'elephant', 'a', 'giraffe', 'dogs', 'python']

# 1. with a while-loop
lst = words.copy()
i = 0
while i < len(lst):
    if len(lst[i]) <= 4:
        lst.pop(i)      # don't increase i: the next element moved into position i
    else:
        i += 1
print(lst)

# 2. with a list comprehension
print([w for w in words if len(w) > 4])
