def merge_sort(List):
    left, right = [], []

    if len(List) <= 1:
        return List

    mid = len(List) // 2

    for i in range(mid):
        left.append(List[i])

    for i in range(mid, len(List)):
        right.append(List[i])

    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)
    return result


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            del left[0]
        else:
            res.append(right[0])
            del right[0]
    if len(left) > 0:
        for val in left:
            res.append(val)

    if len(right) > 0:
        for val in right:
            res.append(val)
    return res


if __name__ == "__main__":
    ar = [5, 2, 1, 4, 3, 0, 3, 9, 4, 2]
    sorted_ar = merge_sort(ar)
    print(sorted_ar)
    # print(merge([1, 2, 3], [2, 4, 3]))
