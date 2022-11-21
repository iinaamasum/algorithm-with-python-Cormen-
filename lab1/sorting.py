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

    with open("random_input.txt", "a+") as file:
        for val in number_list:
            file.write(str(val) + ",")

    file.close()


if __name__ == "__main__":
    # random_number(5000)
    arr = []
    with open("random_input.txt", "r") as file:
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

    print((end - start))

""" 
b       i       s
1.888   1.022   2.325



 """
