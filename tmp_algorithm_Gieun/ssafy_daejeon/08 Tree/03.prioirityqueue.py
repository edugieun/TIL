from queue import PriorityQueue

data1 = [69, 10, 30, 2, 16, 8, 31, 22]
Q = PriorityQueue()

for val in data1:
    Q.put(val)

while not Q.empty():
    print(Q.get(), end=" ")

print('-------------------------------------------')


data2 = [[5, 69], [6, 10], [1, 30], [3, 2], [4, 16], [0, 8], [7, 31], [10, 22]]
Q = PriorityQueue()

for val in data2:
    Q.put(val)

while not Q.empty():
    print(Q.get(), end=" ")
