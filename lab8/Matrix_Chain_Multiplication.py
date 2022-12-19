from sys import maxsize


def memorizedMatrixChain(p) -> None:
    n = len(p)
    m = [[maxsize for i in range(n)] for j in range(n)]

    return lookUpChain(m, p, 0, n - 1)


def lookUpChain(m, p, i, j):
    if m[i][j] < maxsize:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = (
                lookUpChain(m, p, i, k)
                + lookUpChain(m, p, k + 1, j)
                + p[i] * p[k] * p[j]
            )
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


def matrixChainOrder(p):
    n = len(p)
    m = [[maxsize for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n - 1)] for j in range(1, n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = maxsize

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k] * p[j]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j - 1] = k
    return m, s


def optimalParens(s, i, j):
    if i == j:
        print(f"A{i}")
    else:
        print("(")
        optimalParens(s, i, s[i][j])
        optimalParens(s, s[i][j] + 1, j)
        print(")")


# [30, 35, 15, 5, 10, 20, 25]
print("Total Cost Recursive:", memorizedMatrixChain([1, 4, 5, 10, 7]))
m, s = matrixChainOrder([1, 4, 5, 10, 7])
print("Total Cost Iterative:", m[0][4])
# optimalParens(s, 0, 3)
for val in m:
    print(val)
for val in s:
    print(val)
