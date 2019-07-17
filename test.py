# 함수 선언
def fee(minute, distance):
    # 공식부
    # 총 요금 = 대여 요금 + 보험료 + 주행 요금
    price_total = 0
    # 대여 요금 = minute / 10 * 1200
    price_rent = minute / 10 * 1200
    # 보험료 부분 : (minute // 30) * 525 그리고 (minute % 30) != 0 이면 + 525
    price_ins = (minute // 30) * 525
    if (minute % 30) != 0:
        price_ins += 525
    # 주행 요금 부분 : 100km 까지 170원. 그 이후부터는 85원
    if distance <= 100:
        price_dis = distance * 170
    else:
        price_dis = distance // 100 * 170 + distance % 100 * 10 * 85
        
    price_total = price_rent + price_ins + price_dis
    return price_total


print(fee(600, 110))