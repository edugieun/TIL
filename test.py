def lonely(arg):
    # 리스트에 있는 중복을 제거하여 딕셔너리 형태로 만드는 함수는 set()
    # 하지만 set은 알파벳 순서로 딕셔너리를 만들기 때문에 리스트의 순서가 바뀜
    """
    new_arg = list(set(arg)) # set은 딕셔너리 형태이므로 다시 list 형변환
    return new_arg
    """
    # 리스트의 요소를 확인하면서 빈 리스트에 중복되지 않게 담아 다시 만들기
    # ///변수부
    new_list = [] # 빈 리스트 생성
    ex_factor = None
    # ///조건부
    # 리스트 arg의 요소를 모두 확인
    for factor in arg:
        """
        # 빈 리스트에 arg의 요소가 없으면 추가
        if factor not in new_list:
        """
        # 아. 중복을 지우는게 아니라 연속된 요소를 지우는 거네.
        # 그러면, 직전에 빈 리스트에 넣은 요소랑 비교해서 같으면 안 넣는 조건
        # 직전 요소와 이번 요소를 비교할 수 있는 변수가 필요. -> ex_factor = None
        if factor != ex_factor:
            new_list.append(factor) # append()는 리스트에 요소를 추가하는 내장 함수
    return new_list
    
   

