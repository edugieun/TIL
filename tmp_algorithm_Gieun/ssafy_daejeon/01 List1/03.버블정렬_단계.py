
arr = [55, 7, 78, 12, 42]

for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

print(arr)


for i in range(1, len(arr) - 1):
    if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

print(arr)


for i in range(1, len(arr) - 2):
    if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]


print(arr)
