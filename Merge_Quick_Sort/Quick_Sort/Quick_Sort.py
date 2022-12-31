def quick_sort(ar, left, right):
    if left < right:
        pivot = partition(ar, left, right)
        quick_sort(ar, left, pivot - 1)
        quick_sort(ar, pivot + 1, right)
    return ar


def partition(ar, left, right):
    pivot_val = ar[right]
    start_idx = left

    for i in range(left, right):
        if ar[i] <= pivot_val:
            ar[i], ar[start_idx] = ar[start_idx], ar[i]
            start_idx += 1

    ar[start_idx], ar[right] = ar[right], ar[start_idx]
    return start_idx


if __name__ == "__main__":
    ar = [5, 2, 1, 4, 3, 0, 3, 9, 4, 2]
    print(quick_sort(ar, 0, len(ar) - 1))
