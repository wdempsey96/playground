"""Bubble sort implementation."""

UNSORTED_ARRAY = [5, 2, 4, 3, 1, 8, 10, 103, 69, 420, 17, 6, 88, 16, 191]

print("Unsorted array: ", UNSORTED_ARRAY)
print("Sorting...")

is_sorted = False
swapped = False

while not is_sorted:
    i = 0
    is_sorted = True
    while i < len(UNSORTED_ARRAY) - 1:
        if UNSORTED_ARRAY[i+1] < UNSORTED_ARRAY[i]:
            # swap values
            temp = UNSORTED_ARRAY[i+1]
            UNSORTED_ARRAY[i+1] = UNSORTED_ARRAY[i]
            UNSORTED_ARRAY[i] = temp
            is_sorted = False
        i += 1

print("Sorted array: ", UNSORTED_ARRAY)
