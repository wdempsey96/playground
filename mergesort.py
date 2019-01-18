"""Mergesort implementation."""


def mergesort(arr, left, right):
    if left == right:
        print(left, right)
        return [arr[left]]

    middle = int((left + right - 1) / 2)
    left_sorted = mergesort(arr, left, middle)
    right_sorted = mergesort(arr, middle + 1, right)

    return merge(left_sorted, right_sorted)


def merge(left_arr, right_arr):
    print("Merging {} and {}".format(left_arr, right_arr))

    arr = []

    i = 0
    j = 0
    while j < len(right_arr):
        if i < len(left_arr):
            if right_arr[j] < left_arr[i]:
                arr.append(right_arr[j])
                j += 1
            else:
                arr.append(left_arr[i])
                i += 1
        else:
            arr.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        arr.append(left_arr[i])
        i += 1

    print("Merged array: {}".format(arr))

    return arr


UNSORTED_ARRAY = [6, 4, 1, 7, 2, 3, 0, 5, 81, 18, 999, 205, 63, 24, 22, 91, 82]
print("Sorted array: {}".format(mergesort(UNSORTED_ARRAY,
                                          0,
                                          len(UNSORTED_ARRAY) - 1))
)
