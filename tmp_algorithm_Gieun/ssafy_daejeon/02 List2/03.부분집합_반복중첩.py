N = 4
bit = [0] * N

for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            for i in range(2):
                bit[3] = i
                print(bit)

