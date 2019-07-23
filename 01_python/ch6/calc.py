# calc.py
def my_sum(num1, num2):
	return num1 + num2

def my_sub(num1, num2):
	return num1 - num2

def my_mul(num1, num2):
	return num1 * num2

def my_div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.' # 문제에 '반환하시오.'라고 했으니 print가 아니라 return