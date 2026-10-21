def read_words_from_url(url):
    import requests
    
    response = requests.get(url, stream=True)
    words = [line.decode('utf-8').strip() for line in response.iter_lines()]
    
    return words

url = 'https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt'

def sequential_search(key, array):
    for i in range(len(array)):
        if array[i] == key:
            return True
    return False

def binary_search(key, array):    
    low = 0
    high = len(array) - 1
    i = (low + high) // 2
    while low <= high:
        if array[i] == key:
            return True
        elif array[i] < key:
            low = i + 1
        else:
            high = i - 1
        i = (low + high) // 2
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

#print the last 5 words in the dictionary.
'''for i in range(-1, -6, -1):
    print(read_words_from_url(url)[i])'''

key = input("Enter a word to search for: ")
array = read_words_from_url(url)
method = input("Enter the search method (sequential or binary): ")
if method == 'sequential':
    found = sequential_search(key, array)
    time = time_search(sequential_search, len(array))
elif method == 'binary':
    array.sort()
    found = binary_search(key, array)
    time = time_search(binary_search, len(array), sort_data=True)

print(f'By using {method}, the word {key} was {"found" if found else "not found"}, and it takes {time} to search for it.')


