import heapq

data = [69, 10, 30, 2, 16, 8, 31, 22]

arr = []
heapq.heapify(arr)

for val in data:
    heapq.heappush(arr, val)

while arr:
    val = heapq.heappop(arr)
    print(val, end=" ")

print()

arr.clear()
heapq.heapify(arr)

for val in data:
    heapq.heappush(arr, [-val, val])

while arr:
    p, val = heapq.heappop(arr)
    print(val, end=" ")
