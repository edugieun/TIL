arr = [64, 25, 10, 22, 11]

minIdx = 0
for j in range(1, len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[0], arr[minIdx] = arr[minIdx], arr[0]


minIdx = 1
for j in range(2, len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[1], arr[minIdx] = arr[minIdx], arr[1]


print(arr)