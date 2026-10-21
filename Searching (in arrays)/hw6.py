#2.1 i = 2
#2.2 k < vl: i will be negative
#2.2 k> vh: i will be greater than the length of the array
#vi = vl = vh

#implementation of interpolation search
def interpolation_search(key, array):
    if key < array[0] or key > array[-1]:
        return False
    low = 0
    high = len(array) - 1
    i = 0
    while low <= high:
        i = low + ((key- array[low]) * (high - low) // (array[high] - array[low]))
        if array[i] == key:
            return True
        elif array[i] < key:
            low = i + 1
        else:
            high = i - 1
    return False

def time_search(algo, n, /, sort_data = False):
    import random, time

    data = random.choices(range(n), k = n)
    if sort_data: data.sort()
    key = n

    start = time.process_time()
    algo(key, data)
    end = time.process_time()

    return end - start

key = int(input("Enter a number to search for: "))
array = list(range(1000000)) # Example array of integers from 0 to 999999
found = interpolation_search(key, array)
time = time_search(interpolation_search, len(array))
print(f'By using interpolation search, the number {key} was {"found" if found else "not found"}, and it takes {time} to search for it.')
