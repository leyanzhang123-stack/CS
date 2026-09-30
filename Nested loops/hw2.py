# the purpose is to check if there are identical values in two lists.
# not efficient: it doesn't stop when it finds a match, it keeps traversing both lists to the end
flag = False
i = 0
A = [1, 1, 2, 0, 4]
B = [0, 0, 0, 0, 0, 0]
while not flag and i < len(A):
    if A[i] in B:
        flag = True
    i += 1
print(flag)