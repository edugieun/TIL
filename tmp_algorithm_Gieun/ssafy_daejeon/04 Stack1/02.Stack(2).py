

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top = -1

    def push(self, item):
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        ret = self.arr[self.top]
        self.top -= 1
        return ret

    def isEmtpy(self):
        return self.top == -1


S = Stack(10)

for i in range(5):
    S.push(i)


while not S.isEmtpy():
    print(S.pop(), end=" ")
print()
