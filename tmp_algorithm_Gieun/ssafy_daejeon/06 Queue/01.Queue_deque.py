from collections import deque


Q = deque()
for i in range(5):
    Q.append(i)

while len(Q) > 0:
    print(Q.popleft())



test = [() for _ in range(5)]
test[0] = (0, 0)
test[1] = (1, 1)
a = (3, 3)
test[3] = a
print(test)