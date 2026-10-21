# 1.1 7
# 1.2 2
# 2
def bin_search(key, array):
    found = False
    low = 0
    high = len(array) - 1
    lst = []
    #change the values of low and high until they cross each other
    while not found and low <= high:
        i = (low + high) // 2 #i = midpoint
        lst.append(array[i])
        if array[i] == key:
            found = True
            #if not using found, then "return True" jumps out of the function
        elif array[i] < key:
            low = i + 1
        else: #array[i] > key
            high = i - 1 #more efficient than high = i
    return found, lst

key = 'Max'
array = ['Alissa', 'Ben', 'Cate', 'David', 'Eva', 'Max', 'Sam', 'Zoe']
print(bin_search(key, array))