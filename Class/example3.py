def find_all(s, sub):
    start = 0
    result = []
    while (m := s.find(sub, start)) != -1:
        result.append(m)
        start = m + 1
    return result

s = 'ababab'
print(find_all(s, 'aba'))
print(find_all(s, 'ab'))
print(find_all(s, 'b'))