def seq_search(key, array):
    found = False
    i = 0
    while not found and i < len(array):
        if array[i] == key:
            found = True
        i += 1
    return found

def time_search(seq_search, n, /, sort_data = False):
    import random, time

    data = random.choices(range(n), k = n)
    if sort_data: data.sort()
    key = n

    start = time.process_time()
    seq_search(key, array)
    end = time.process_time()

    return end - start

array = [1, 2, 3, 4, 5, 6, 7]
print(seq_search(, array), time_search(seq_search, 7))
