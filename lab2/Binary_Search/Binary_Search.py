def binary_search(arr, searching):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == searching:
            return True
        elif arr[mid] < searching:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, -1))
