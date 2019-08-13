class BinaryHeap(object):
    def __init__(self):
        self.arr = [0]
        
    def isEmpty(self):
        return len(self.arr) == 1

    def push(self, item):
        self.arr.append(item)

        c = len(self.arr) - 1
        p = int(c/2)
        while p > 0:
            if self.arr[c] < self.arr[p]:
                self.arr[c], self.arr[p] = self.arr[p], self.arr[c]
                c = p
                p = int(c/2)
            else:
                break

    def pop(self):
        ret = self.arr[1]
        self.arr[1] = self.arr[-1]

        p, c = 1, 2
        last = len(self.arr) - 1
        while c <= last:
            if c + 1 <= last and self.arr[c] > self.arr[c + 1]:
                c += 1
            if self.arr[c] < self.arr[p]:
                self.arr[c], self.arr[p] = self.arr[p], self.arr[c]
                p = c
                c = p * 2
            else:
                break
        self.arr.pop()
        return ret

data =  [69, 10, 30, 2, 16, 8, 31, 22]
Q = BinaryHeap()

for val in data:
    Q.push(val)

while not Q.isEmpty():
    print(Q.pop(), end=" ")
