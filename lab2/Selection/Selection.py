from sys import maxsize


def select(array, n, k):
    low, up = 0, n + 1
    array.append(maxsize)
