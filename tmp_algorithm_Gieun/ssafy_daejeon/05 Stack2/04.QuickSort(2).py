
def quickSort(arr, lo, hi):
    if lo < hi:
        i, j = lo, hi

        while i < j:
            while i <= hi and arr[i] <= arr[lo]:
                i += 1

            while arr[j] > arr[lo]:
                j -= 1

            if i >= j: break

            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]

        quickSort(arr, lo, j - 1)
        quickSort(arr, j + 1, hi)


arr = [69, 10, 30, 2, 16, 8, 31, 22, 30]
quickSort(arr, 0, len(arr) - 1)
print(arr)
