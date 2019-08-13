
N = 5
arr = []


def push(item):
    arr.append(item)


def pop():
    return arr.pop()


for i in range(5):
    push(i)


while len(arr) > 0:
    print(pop(), end=" ")
print()
