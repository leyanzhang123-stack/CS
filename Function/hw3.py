def read_ints():
    lst = []
    while True:
        user_input = input("Enter integer (or press Enter to finish): ")
        if user_input == "":
            break
        else:
            lst.append(int(user_input))
    return lst

print(read_ints())