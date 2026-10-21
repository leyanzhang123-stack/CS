students = ['Alissa', 'Ben', 'Charlie', 'Diana']
grades = ['B', 'D', 'B', 'A']

found = False
i = 0
while not found and i < len(students):
    if students[i] == 'Charlie':
        found = True
    i += 1
print(grades[i - 1])