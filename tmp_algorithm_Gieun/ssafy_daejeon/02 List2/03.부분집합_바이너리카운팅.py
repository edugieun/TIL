arr = [3, 6, 7, 1, 5, 4]

for i in range(1 << len(arr)):  # i: 집합의 비트 표현
    for j in range(len(arr)):
        if i & (1 << j):
            print(arr[j], end=", ")

    print()

