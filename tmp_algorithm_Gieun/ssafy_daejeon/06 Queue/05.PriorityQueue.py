from heapq import heappush, heappop

H = []
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

for val in arr:
    heappush(H, val)

while len(H) > 0:
    print(heappop(H), end=" ")
print()
