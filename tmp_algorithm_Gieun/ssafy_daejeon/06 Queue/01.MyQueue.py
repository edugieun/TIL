class myQ:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = -1
        self.rear = -1

    def push(self, item):
        self.rear += 1
        self.arr[self.rear] = item

    def pop(self):
        self.front += 1
        return self.arr[self.front]

    def empty(self):
        return self.front == self.rear


Q = myQ(100)
for i in range(10):
    Q.push(i)
while not Q.empty():
    print(Q.pop(), end=' ')
