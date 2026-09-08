while a:
    lst = []
    word = input("Enter a word (or ! to finish): ")
    if word == "!":
        a = False
    lst.append(word)
lst_original = lst

a = True
while a:
    ind = []
    index = int(input("Enter an index: "))
    if index < 0:
        a = False
    ind.append(index)

for i in range(len(ind)):
    lst.remove(lst[ind[i]])

print(lst_original)
print(ind)
print(lst)