def quick_sort(List, left, right):
    if right > left:
        pivot = left
        pivot = partition(List, left, right, pivot)
        quick_sort(List, left, pivot - 1)
        quick_sort(List, left, pivot + 1)


def partition(ar, left, right, pivot):
    pivot_val = ar[pivot]
    ar[pivot], ar[right] = ar[right], ar[pivot]

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
