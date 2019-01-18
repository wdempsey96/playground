"""Quicksort implementation."""


def quicksort(arr, left, right):
    # base case
    if left >= right:
        return

    partition_index = partition(arr, left, right)

    # inductive step
    quicksort(arr, left, partition_index - 1)  # left of partition
    quicksort(arr, partition_index + 1, right)  # right of partition


def partition(arr, left, right):
    pivot = right
    i = left - 1

    for j in range(left, right):
        if arr[j] <= arr[pivot]:
            i += 1
            swap(arr, i, j)
            print("Swapping {} and {}\n{}".format(arr[i], arr[j], arr))

    swap(arr, i + 1, pivot)
    print("Swapping {} and {}\n{}".format(arr[i+1], arr[pivot], arr))

    return i + 1


def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


UNSORTED_ARRAY = [6, 4, 1, 7, 2, 3, 0, 5]
quicksort(UNSORTED_ARRAY, 0, len(UNSORTED_ARRAY) - 1)
print("Sorted array: {}".format(UNSORTED_ARRAY))
