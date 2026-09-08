def sum_upto(n):
    return n * (n + 1) // 2

for i in range(1, 21):
    print(f'The sum of the first {i} positive integers is: {sum_upto(i)}')