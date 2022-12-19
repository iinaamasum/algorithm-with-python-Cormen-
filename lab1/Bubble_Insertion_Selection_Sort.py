import random
import time


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # swap val
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            # swap with min
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = val


def random_number(number):
    number_list = []
    while number:
        number_list.append(random.randint(0, 100000))
        number -= 1

    with open("test.txt", "a+") as file:
        for val in number_list:
            file.write(str(val) + ",")

    file.close()


if __name__ == "__main__":
    random_number(5000)
    arr = []
    with open("test.txt", "r") as file:
        file_inputs = list(map(str, file.read().split(",")))
    file.close()

    for val in file_inputs:
        if val != "":
            arr.append(int(val))

    start = time.time()
    bubble_sort(arr)
    # insertion_sort(arr)
    # selection_sort(arr)
    end = time.time()

    with open("binary_5.txt", "a+") as file:
        for val in arr:
            file.write(str(val) + ",")

    print((end - start))

""" 
input      b       i       s
5000     1.690   0.857   1.556
10000    6.654   3.557   6.033
15000    14.732  7.978   13.955
20000    27.002  14.393  25.538  
 """
