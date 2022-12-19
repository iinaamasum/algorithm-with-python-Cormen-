def LCS(x, y):
    m, n = len(x), len(y)
    b = [["" for i in range(0, m + 1)] for j in range(0, n + 1)]
    c = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, m):
        c[i][0] = 0
    for j in range(n):
        c[0][j] = 0
    # print(m)
    for i in range(1, m):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "d"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "u"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "l"
    return c, b


x, y = "ABCBDAB", "BDCABA"
c, b = LCS(x, y)
print("LCS size is:", c[len(x) - 1][len(y)])
print("C:")
for val in c:
    print(val)
print("B: ")
for val in b:
    print(val)
