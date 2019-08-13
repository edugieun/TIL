
ROW, COL = 5, 5
arr = [[0 for _ in range(COL)] for _ in range(ROW)]
visit = [[False for _ in range(COL)] for _ in range(ROW)]

def spiralTraverse(dir, x, y, cnt):

    if x < 0 or y < 0 or x == ROW or y == COL: return
    if visit[x][y]: return

    visit[x][y] = True
    arr[x][y] = cnt

    if dir == 0:
        spiralTraverse(0, x, y + 1, cnt + 1)
        spiralTraverse(1, x + 1, y, cnt + 1)
    elif dir == 1:
        spiralTraverse(1, x + 1, y, cnt + 1)
        spiralTraverse(2, x, y - 1, cnt + 1)
    elif dir == 2:
        spiralTraverse(2, x, y - 1, cnt + 1)
        spiralTraverse(3, x - 1, y, cnt + 1)
    else:
        spiralTraverse(3, x - 1, y, cnt + 1)
        spiralTraverse(0, x, y + 1, cnt + 1)


spiralTraverse(0, 0, 0, 1)

for i in range(ROW):
    for j in range(COL):
        print("%2d " % arr[i][j], end="")
    print()
