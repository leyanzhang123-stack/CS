def max_char_rep(s):  # FIX: name was max_chat_rep
    if s == '':  # FIX: the empty string must give 0 (before it gave 1)
        return 0
    max = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max: max = count
    return max

s = input("Enter a string:")
print(max_char_rep(s))
