# input example 1
# 1
# 5
# 2 3 5 1 4
# 1, 2, 5, 4, 3
# input example 2
# 1
# 7
# 1 2 3 4 5 6 7
# expected: 1, 2, 3, 7, 6, 5, 4
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


test_cases = [
    [2, 3, 5, 1, 4],
    [1, 2, 3, 4, 5, 6, 7]
]
for a in test_cases:
    findZigZagSequence(a, len(a))
