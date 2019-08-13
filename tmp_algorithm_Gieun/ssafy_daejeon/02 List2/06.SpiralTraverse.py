
ROW, COL = 5, 5
arr = [[0 for _ in range(COL)] for _ in range(ROW)]

row_start = col_start = 0
row_end, col_end = ROW - 1, COL - 1

cnt = 0
while row_start <= row_end and col_start <= col_end:
    # 오른쪽 이동
    i = col_start
    while i <= col_end:
        cnt += 1
        arr[row_start][i] = cnt
        i += 1

    row_start += 1

    # 아래로 이동
    i = row_start
    while i <= row_end:
        cnt += 1
        arr[i][col_end] = cnt
        i += 1
    col_end -= 1

    # 왼쪽 이동
    i = col_end
    while i >= col_start:
        cnt += 1
        arr[row_end][i] = cnt
        i -= 1

    row_end -= 1
    # 위로 이동
    i = row_end
    while i >= row_start:
        cnt += 1
        arr[i][col_start] = cnt
        i -= 1
    col_start += 1


for i in range(ROW):
    for j in range(COL):
        print("%2d " % arr[i][j], end="")
    print()
