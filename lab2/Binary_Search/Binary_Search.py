import time


def binary_search(arr, searching):
    low = 0
    high = len(arr) - 1
    print(high)
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
    with open("binary_1.txt", "r") as file:
        arr = list(map(str, file.read().split(",")))
    file.close()

    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except:
            del arr[i]
    start = time.time()
    print(binary_search(arr, 47345))
    end = time.time()

    print((end - start) * 1000)
