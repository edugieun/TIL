from queue import Queue

Q = Queue()
for i in range(5):
    Q.put(i)

while not Q.empty():
    print(Q.get())



