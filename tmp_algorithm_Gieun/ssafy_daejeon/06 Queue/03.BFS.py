from queue import Queue

def BFS(s, G):

    visit = [False] * (V + 1)
    D = [0] * (V + 1)

    Q = Queue()
    Q.put(s)
    visit[s] = True
    print(s, end=" ")
    while not Q.empty():
        v = Q.get()
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                Q.put(w)
                print(w, end=" ")
    print()
    return D
# ----------------------------------------------

import sys
sys.stdin = open("BFS_input.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


D = BFS(1, G)

print(D[1:])