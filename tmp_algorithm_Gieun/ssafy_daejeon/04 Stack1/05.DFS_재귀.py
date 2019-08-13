def DFS(v):
    visit[v] = True

    print(v, end=" ")
    
    for w in G[v]:
        if not visit[w]:
            DFS(w)

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