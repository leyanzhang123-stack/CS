def bin_search(key, array):
    found = False
    low = 0
    high = len(array) - 1
    #change the values of low and high until they cross each other
    while not found and low <= high:
        i = (low + high) // 2 #i = midpoint
        if array[i] == key:
            found = True
            #if not using found, then "return True" jumps out of the function
        elif array[i] < key:
            low = i + 1
        else: #array[i] > key
            high = i - 1 #more efficient than high = i
    return found

key = 'Max'
array = ['Alissa', 'Ben', 'Max', 'Sam', 'Zoe']
print(bin_search(key, array))

'''
steps | remaining
0 n
1 n/2
2 n/4
3 n/8
...
k n/(2^k)
when n/(2^k) = 1, then n = 2^k, so k = log2(n)
->O(log2(n)) is much much faster than linear search, which is O(n)
'''