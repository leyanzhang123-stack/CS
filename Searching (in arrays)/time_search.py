def time_search(algo, n, /, sort_data = False):
    import random, time

    data = random.choices(range(n), k = n)
    if sort_data: data.sort()
    key = n

    start = time.process_time()
    algo(data, key)
    end = time.process_time()

    return end - start