a = 0
lst = []
seen = []
while a >= 0:
    a = int(input("Please enter a nonnegative number: "))
    if a >= 0:
        lst.append(a)
print(lst)
for i in range(len(lst)): 
    if not (lst[i] in seen):
        print(lst[i], end=" ")
        seen.append(lst[i])