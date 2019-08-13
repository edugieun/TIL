from queue import Queue

def BFS(s, G):

    D[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put(v)

    print()
# ----------------------------------------------

import sys
sys.stdin = open("weighted_graph.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0xfffff] * (V + 1)
P = [i for i in range(V + 1)]


for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


BFS(1, G)

print(D[1:])
print(P[1:])