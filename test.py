# 강사님 코드
# 양의 정수 n 을 입력 받아 제곱근의 근사값(제곱했을 때 n이 되는 수)를 반환하는 함수를 작성.
def my_sqrt(n):   # 2
    # 왼쪽 수를 그냥 1로 잡아버림.   
    x, y = 1, n
    result = 1    
    # 제곱근의 제곱(result**2)과 입력 값(n)의 차이가 적어도 이 정도 차이보다 작아지면!
    while abs(result**2 - n) > 1e-10: 
    # 위의 while 조건은 다음도 됨. while not math.isclose(result**2, n):
    # 단, import math 해야함.
        result = (x+y)/2 # 양쪽 끝 값을 더해서 2로 나눈다(절반을 구한다)
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))