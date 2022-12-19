import random
import time


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
    with open(f"random_num_{number}.txt", "w") as file:
        for i in range(number):
            file.write(str(random.randint(1, 100000)) + ",")
    file.close()


if __name__ == "__main__":
    # random_number(25000)

    # read files and convert input into int val
    with open("random_num_25000.txt", "r") as file:
        arr = list(map(str, file.read().split(",")))
    file.close()

    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except:
            del arr[i]
    # recur_start_time = time.time()
    # res = linear_search_recursive(arr, searching)
    # recur_end_time = time.time()

    # with open("recursive_time.txt", "a") as file:
    #     file.write(str(recur_end_time - recur_start_time) + ",")
    # file.close()

    searching = 1
    iter_start_time = time.time()
    linear_search_iterative(arr, searching)
    iter_end_time = time.time()
    print((iter_end_time - iter_start_time) * 1000)
    with open("iter_time_b.txt", "a") as file:
        file.write(str(round((iter_end_time - iter_start_time) * 1000, 3)) + ",")
    file.close()

    searching = -111111
    iter_start_time = time.time()
    linear_search_iterative(arr, searching)
    iter_end_time = time.time()

    with open("iter_time_w.txt", "a") as file:
        file.write(str(round((iter_end_time - iter_start_time) * 1000, 3)) + ",")
    file.close()

    searching = -11000
    iter_start_time = time.time()
    linear_search_iterative(arr, searching)
    iter_end_time = time.time()

    with open("iter_time_avg.txt", "a") as file:
        file.write(str(round((iter_end_time - iter_start_time) * 1000, 3)) + ",")
    file.close()

    # if res:
    #     print(f"{searching} is found.")
    # else:
    #     print(f"{searching} is not found.")
