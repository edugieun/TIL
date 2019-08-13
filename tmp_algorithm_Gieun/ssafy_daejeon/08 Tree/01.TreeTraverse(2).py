import sys
sys.stdin = open('tree_input.txt')

def inorder(v):
    if v == 0: return

    inorder(tree[v][0])
    print(v, end=' ')
    inorder(tree[v][1])


V, E = map(int, input().split())
tree = [[0, 0, 0] for _ in range(V + 1)]
arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]

    if tree[u][0] == 0:
        tree[u][0] = v
    else:
        tree[u][1] = v
    tree[v][2] = u


inorder(1)

