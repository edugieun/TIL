import sys
sys.stdin = open('tree_input.txt')

def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])


V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]

    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v
    P[v] = u


inorder(1)

