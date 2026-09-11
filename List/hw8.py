a = True
lst = []
while a:
    word = input("Enter a word (or ! to finish): ")
    if word == "!":
        a = False
        break
    lst.append(word)
''' 
while(word := input("Enter a word (or ! to finish) != "!"):
    lst.append(word)
'''
lst_original = lst.copy()
ind = []
a = True
while a:
    index = int(input("Enter an index: "))
    if index < 0:
        a = False
        break
    ind.append(index)
    lst[index] = "!"
while "!" in lst:
    lst.remove("!")
print(lst_original)
print(ind)
print(lst)


