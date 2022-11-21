import random


def linear_search_iterative(arr, searching):
    for val in arr:
        if val == searching:
            return True

    return False


def linear_search_recursive(arr, searching, idx=0):
    if idx >= len(arr):
        return False
    if arr[idx] == searching:
        return True
    idx += 1
    return linear_search_recursive(arr, searching, idx)


# random number generation
def random_number(number):
    with open("random_num.txt", "a") as file:
        for i in range(number):
            file.write(str(random.randint(214, 100000)) + ",")
    file.close()


if __name__ == "__main__":
    random_number(10)

    # read files and convert input into int val
    with open("random_num.txt", "r") as file:
        arr = list(map(str, file.read().split(",")))
    file.close()

    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except:
            del arr[i]
    searching = 8344
    res = linear_search_recursive(arr, searching)
    if res:
        print(f"{searching} is found.")
    else:
        print(f"{searching} is not found.")
