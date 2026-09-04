def swap(lst, ind1, ind2):
    lst[ind1], lst[ind2] = lst[ind2], lst[ind1]
    return lst

lst = list(map(int, input("enter a list: ").split()))
ind1 = int(input("enter the first index: "))
ind2 = int(input("enter the second index: "))
if ind1 < 0 or ind1 >= len(lst) or ind2 < 0 or ind2 >= len(lst):
    print("Error: Indices must be within the range of the list.")
else:
    print(swap(lst, ind1, ind2))