
arr = "ABCD"
order = []      # 순열 저장
cnt = 1

def perm(k, n, used):
    if k == n:
        global cnt
        print("%2d> %s" % (cnt, " ".join(order)))
        cnt += 1
        return

    for i in range(n):
        if used & (1 << i): continue

        order.append(arr[i])

        perm(k + 1, n, used | (1 << i))

        order.pop()


perm(0, 4, 0)
