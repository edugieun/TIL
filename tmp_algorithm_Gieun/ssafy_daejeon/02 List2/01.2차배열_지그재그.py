
arr = [[ 1,  2,  3,  4,  5],
    [10,  9,  8,  7,  6],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16],
    [21, 22, 23, 24, 25]]



N, M = len(arr), len(arr[0])
for i in range(N):
    if i & 1 == 0:
        for j in range(M):
            print('%2d ' % arr[i][j], end='')
    else:
        for j in range(M - 1, -1, -1):
            print('%2d ' % arr[i][j], end='')
    print()

