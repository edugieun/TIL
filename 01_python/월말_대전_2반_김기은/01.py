# 파일명 및 함수명을 변경하지 마시오.
def can_divide(numbers, divisor):
    """
    아래에 코드를 작성하시오.
    numbers는 0이 아닌 양의 정수가 담긴 리스트입니다.
    divisor는 0이 아닌 양의 정수입니다.
    numbers에 담겨있는 숫자들 중, divisor로 나누어 떨어지는 숫자들을 오름차순으로 정렬한 리스트를 반환합니다.
    """
    new_list = []

    for number in numbers:
        if number%divisor == 0:
            new_list.append(number)
    
    if bool(new_list) == False:
        new_list.append(-1)
        return new_list
    else:
        return sorted(new_list)






# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(can_divide([20, 3, 5, 7], 5))
    print(can_divide([4, 3, 2, 1], 1))
    print(can_divide([7, 11, 13], 3))
