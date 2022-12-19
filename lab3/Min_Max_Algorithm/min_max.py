def simpleMinMax(array, min_val, max_val):
    for val in array:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    return min_val, max_val


def minMaxAlgoDAC(array, min_val, max_val, left, right):
    i, j = left, right

    # termination condition
    if i == j:
        return min_val, max_val
    elif i == j - 1:
        min_val = min(array[i], array[j])
        max_val = max(array[i], array[j])
        return min_val, max_val

    # processing data
    else:
        mid = (i + j) // 2
        min_val1, max_val1 = minMaxAlgoDAC(array, min_val, max_val, i, mid)
        min_val, max_val = minMaxAlgoDAC(array, min_val1, max_val1, mid + 1, j)

        min_val = min(min_val1, min_val)
        max_val = max(max_val1, max_val)

        return min_val, max_val


def generateRandomNumber(num):
    pass


if __name__ == "__main__":
    a = []
    # reading data from file
    with open("random_input.txt") as file:
        for val in file:

            i = val.strip().split(",")
            for num in i:
                try:
                    a.append(int(num))
                except:
                    continue
    file.close()

    min_val = max_val = a[0]
    print("Min Max:", simpleMinMax(a, min_val, max_val))

    left, right = 0, len(a) - 1
    print("DAC Min Max:", minMaxAlgoDAC(a, min_val, max_val, left, right))
