arr = [[1,  6, 11, 16, 21],
[2,  7, 12, 17, 22],
[3,  8, 13, 18, 23],
[4,  9, 14, 19, 24],
[5, 10, 15, 20, 25]]

N, M = len(arr), len(arr[0])
for i in range(N):
    for j in range(M):
        print('%2d ' % arr[j][i], end='')
    print()

