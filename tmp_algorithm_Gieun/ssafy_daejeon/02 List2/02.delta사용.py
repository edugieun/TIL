
arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]

N, M = len(arr), len(arr[0])

# dx, dy 각각 리스트로 저장
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sum = 0
for x in range(N):
    for y in range(M):
        for i in range(len(dx)):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or ty < 0 or tx == len(arr) or ty == len(arr[0]):
                continue

            val = arr[x][y] - arr[tx][ty]
            sum += (-val if val < 0 else val)

print(sum)

# set 으로 저장
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

sum = 0
for x in range(N):
    for y in range(M):
        for dx, dy in delta:
            tx, ty = x + dx, y + dy
            if tx < 0 or ty < 0 or tx == len(arr) or ty == len(arr[0]):
                continue

            val = arr[x][y] - arr[tx][ty]
            sum += (-val if val < 0 else val)

print(sum)