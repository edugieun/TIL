# 4장 연습문제2

def check_paren(exp):
    stack = []

    for ch in exp:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False

    return True

str1 = '()()((()))'
str2 = '((()((((()()((()())((()))))'

if check_paren(str2):
    print('OK')
else:
    print('FAIL')
