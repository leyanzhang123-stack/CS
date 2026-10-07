def seq_search(key, array):
    found = False
    i = 0
    while not found and i < len(array):
        if array[i] == key:
            found = True
        i += 1
    return found

def time_search(algo, n, /, sort_data = False):
    import random, time

    data = random.choices(range(n), k = n)
    if sort_data: data.sort()
    key = n

    start = time.process_time()
    algo(key, array)
    end = time.process_time()

    return end - start

array = [1, 2, 3, 4, 5, 6, 7]
print(time_search(seq_search, 10 ** 6))
