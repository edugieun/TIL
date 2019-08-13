# 정수를 문자열로 변환
num = int(input("정수 입력: "))

# str() 함수 사용
numstr = str(num)
print(numstr)


# /, % 연산자 사용
numstr = ''

if num == 0:
    numstr = '0'
else:
    while num > 0:
        digit = num % 10
        num = num//10
        numstr += str(digit)

numstr = numstr[::-1]

print(numstr)

