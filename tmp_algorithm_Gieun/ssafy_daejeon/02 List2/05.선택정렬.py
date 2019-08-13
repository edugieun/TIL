arr = [64, 25, 10, 22, 11]

for i in range(len(arr) - 1):
    minIdx = i
    for j in range(i + 1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j

    arr[i], arr[minIdx] = arr[minIdx], arr[i]


print(arr)