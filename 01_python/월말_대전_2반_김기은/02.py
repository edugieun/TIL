# 파일명 및 함수명을 변경하지 마시오.
def alphabet_count(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성되어 있습니다.
    알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    """
    alpha_dict = {}

    for char in word:
        if char not in alpha_dict.keys():
            alpha_dict[char] = 1
        else:
            for key, value in alpha_dict.items():
                if char == key:
                    alpha_dict[key] = value + 1
    return alpha_dict
    






# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
