"""Returns the nth smallest elment of input list."""


INPUT = [10, 2, 5, 6, 11, 3, 15]
N = 3


index = 0
for i, val in enumerate(INPUT):
    if i == 0:
        pass
    else:
        if val < INPUT[index]:
            # swap the values
            INPUT[i] = INPUT[index]
            INPUT[index] = val
            index += 1
        else:
            # update index
            index = i
print(INPUT)

