def seq_search(key, array):
    found = False
    i = 0
    while not found and i < len(array):
        if array[i] == key:
            found = True
        i += 1
    return found
#lines to execute 2(found and i initialize)+4n(every loop)+1(found=True)+1(return) = 4n+4

def time_search(algo, n, /, sort_data = False):
    import random, time

    data = random.choices(range(n), k = n)
    if sort_data: data.sort()
    key = n

    start = time.process_time()
    algo(key, data)
    end = time.process_time()

    return end - start

array = [1, 2, 3, 4, 5, 6, 7]
print(time_search(seq_search, 10 ** 6))

#f(n) = an+b ≈ an because when n is large, b is negligible
#f(n) is O(n) if f(n)/n ≈ constant when n is large

#let algorithm be O(n) then the number of steps will be approximately an
#So increasing the number of elements by a factor of 10 will increase the running time by a factor of 10 as well
#linear time complexity means that the running time of the algorithm increases linearly with the size of the input data. (worst or average case)

#it is linear not root n or log n because the algorithm has to check each element in the array one by one until it finds the key or reaches the end of the array. This means that the number of steps required to complete the search is directly proportional to the size of the input data, resulting in a linear time complexity of O(n).

