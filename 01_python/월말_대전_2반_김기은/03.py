# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """
    
    result = ''
    count = 0

    for idx in range(len(word)):
        if idx == 0:
            count += 1
        elif word[idx - 1] == word[idx]:
            count += 1
        elif word[idx - 1] != word[idx]:
            result = result + word[idx - 1] + str(count)
            count = 1
    
    result = result + word[-1] + str(count)

    return result


        






# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
