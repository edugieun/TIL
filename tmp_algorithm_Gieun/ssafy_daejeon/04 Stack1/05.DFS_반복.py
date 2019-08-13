def DFS(v):

    stack = []
    stack.append(v)
    visit[v] = True
    print(v, end=" ")

    while len(stack) > 0:
        prev = v
        for w in G[v]:
            if not visit[w]:
                stack.append(w)
                v = w
                visit[w] = True
                print(v, end=" ")
                break
        if prev == v:
            v = stack.pop()

# ----------------------------------------------
import sys

sys.stdin = open("DFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)