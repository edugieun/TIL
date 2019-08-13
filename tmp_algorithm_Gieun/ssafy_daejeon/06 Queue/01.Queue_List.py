
Q = []

Q.append(1)
Q.append(2)
Q.append(3)
print(Q)

print("dequeu = %d" % (Q.pop(0)))
print(Q)

while len(Q) > 0:
    print("dequeu = %d" % (Q.pop(0)))

print(Q)