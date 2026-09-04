a = ''
b = ''
lst = []
#print("stage 1")
while a != '!':
    a = input("Enter a word: ")
    lst.append(a)
#print("stage 2")
while b != '!':
    b = input("Enter a word: ")
    if b in lst and b != '!': print("hit")