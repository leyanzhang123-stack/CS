def max_chat_rep(s):
    max = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            print("yes!")
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    return max

s = input("Enter a string:")
print(max_chat_rep(s))