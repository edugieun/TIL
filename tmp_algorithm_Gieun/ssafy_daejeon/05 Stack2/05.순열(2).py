
arr = "ABCD"
order = []                  # 순열 저장
used = [False] * len(arr)   # 사용된 요소들 정보
cnt = 1

def perm(k, n):
    if k == n:
        global cnt
        print("%2d> %s" % (cnt, " ".join(order)))
        cnt += 1
        return

    for i in range(n):
        if used[i]: continue

        used[i] = True
        order.append(arr[i])

        perm(k + 1, n)

        used[i] = False
        order.pop()


perm(0, 4)
