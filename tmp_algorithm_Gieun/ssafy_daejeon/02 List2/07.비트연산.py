def BitPrint(n):
    for i in range(7, -1, -1):
        print(1 if (n & (1 << i)) else 0, end="")
    print()


for i in range(-5, 6):
    print("%3d = " % i, end="") # 십진수 출력
    BitPrint(i)		            # 이진수 출력


print("-------------------------------------------------\n")

# 라이브러리 사용하기
# int(), bin(), oct(), hex()

for i in range(-5, 6):
    binstr = bin(i)
    deci = int(binstr, 2)
    print(deci, binstr)



