def SetPrint(set, arr):
    for i in range(8):
        if set & (1 << i):
            print(arr[i], end=" ")
    print()


arr = "ABCDEFGH"
A = 0x2D
B = 0x65	# (A C D F), (A C F G)

print("A집합> ", end="")
SetPrint(A, arr)

print("B집합> ", end="")
SetPrint(B, arr)

print(" ~A > ", end="")
SetPrint(~A, arr)

print("합집합> ", end="")
SetPrint(A | B, arr)

print("교집합> ", end="")
SetPrint(A & B, arr)

print("A-B > ", end="")
SetPrint(A & ~B, arr)

print("-----------------------------------------------\n")

# Set 라이브러리 사용하기
A = {'A', 'C', 'D', 'F'}
B = {'A', 'C', 'F', 'G'}

print("A집합> ", end="")
print(A)

print("B집합> ", end="")
print(B)

print("합집합> ", end="")
print(A | B)

print("교집합> ", end="")
print(A & B)

print("A-B > ", end="")
print(A - B)

print("(합집합 - 교집합)> ", end="")
print(A ^ B)

