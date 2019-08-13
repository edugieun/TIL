
arr = [[ 1,  2,  4,  7, 11],
    [ 3,  5,  8, 12, 15],
    [ 6,  9, 13, 16, 18],
    [10, 14, 17, 19, 20]]


N, M = len(arr), len(arr[0])
for diag in range(0, N + M - 1):    # diag: 사선의 수
                                    # x, y: 시작 좌표
    x = 0 if diag < M else (diag - M + 1)
    y = diag if diag < M else M - 1

    while x < N and y >= 0:
        print('%2d ' % arr[x][y], end='')
        x += 1
        y -= 1
    print()


