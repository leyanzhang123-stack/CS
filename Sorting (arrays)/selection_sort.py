def selection_sort(array):
    """
    Steps:
    1. find the smallest element in the array
    2. swap it with the first element of the array
    3. repeat the process in the remaining unsorted portion of the array
    """
    n = len(array)
    #find the smallest element in the array
    for ind in range(n - 1):
        min = array[ind]
        min_index = ind
        for i in range(ind + 1, n):
            v = array[i]
            if v < min:
                min = v
                min_index = i
        #swap for the first time
        array[ind], array[min_index] = array[min_index], array[ind]
    #then, remaining unsorted portion of the array
    return array

def t_selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        smallest = array[i]
        for j in range(i + 1, n):
            if array[j] < smallest:
                smallest = array[j]  
                smallest_ind = j
        #swap if necessary
        if smallest_ind != i:
            (array[i] , array[smallest_ind]) = (array[smallest_ind], array[i])  

def time_sort(algo, n):
    import time, random

    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

import random
n = 2000
arr = [random.randint(0, n) for _ in range(n)]
#print(selection_sort(arr))
print(time_sort(selection_sort, n))