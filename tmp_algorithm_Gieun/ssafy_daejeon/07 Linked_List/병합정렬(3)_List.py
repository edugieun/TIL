def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = int(len(arr) / 2)

    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result += left
    else:
        result += right

    return result


unsort = [69, 10, 30, 2, 16, 8, 31, 22]
sort = mergeSort(unsort)
print(sort)