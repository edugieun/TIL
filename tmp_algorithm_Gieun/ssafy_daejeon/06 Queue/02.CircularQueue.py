QSIZE = 5
Q = [''] * QSIZE
front = rear = 0
def push(item):
    global rear
    if (rear + 1) % QSIZE == front:
        print('Q-Full 상태-->')
        return False
    rear = (rear + 1) % QSIZE
    Q[rear] = item

def pop():
    global front
    front = (front + 1) % QSIZE
    return Q[front]

def empty():
    global front, rear
    return front == rear

def printQ():
    if empty(): return
    i = front
    while i != rear:
        i = (i + 1) % QSIZE
        print(Q[i], end='')
    print()

push('A')
push('B')
push('C')
push('D')
printQ()
push('E')       # Q-FULL 상태
print("삭제-> ", pop())
printQ()
print("삽입-> ")
push('E')
printQ()
print("삭제-> ", pop())
print("삭제-> ", pop())
printQ()
