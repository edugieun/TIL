
def partition(a ,begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while a[L] < a[pivot] and L < R:
            L += 1
        while a[R] >= a[pivot] and L < R:
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]

    return R


def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p - 1)
        quickSort(a, p + 1, end)


arr = [69, 10, 30, 2, 16, 8, 31, 22, 30]
quickSort(arr, 0, len(arr) - 1)
print(arr)
