
def sequence_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key: return i
    return -1

def binarySearch(arr, lo, hi, key):
    if lo > hi: return -1

    mid = (lo + hi) >> 1
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, lo, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, hi, key)

def binary_search(arr, lo, hi, key):
    while lo <= hi:
        mid = (lo + hi) >> 1
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]

hi = len(arr) - 1
print(sequence_search(arr, 39))
print(sequence_search(arr, 50))

print(binary_search(arr, 0, hi, 39))
print(binary_search(arr, 0, hi, 50))

print(binarySearch(arr, 0, hi, 39))
print(binarySearch(arr, 0, hi, 50))

print("---------------------------------------")

# ------------------------------------------------------
# bisect 라이브러리 사용
from bisect import bisect, bisect_left, bisect_right


print(bisect_left(arr, 39))     # bisect()와 혼동하지 말것, 범위 지정 가능
print(bisect_left(arr, 50))     # 결과값 무엇?
print(bisect_right(arr, 45))


