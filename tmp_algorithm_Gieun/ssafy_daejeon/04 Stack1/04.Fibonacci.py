print('---------------------------------------------------')
print('\t재귀')

def fibo(n):
    if n < 2:
        return n

    return fibo(n - 1) + fibo(n - 2)


for i in range(1, 11):
    print('fibo({}) = {}'.format(i, fibo(i)))


print('---------------------------------------------------')
print('\t재귀 + 메모')
memo = [0] * 11
memo[1] = 1

def fibo_memo(n):
    if n < 2 or memo[n]:
        return memo[n]

    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return memo[n]

fibo_memo(10)

for i in range(1, 11):
    print('memo[{}] = {}'.format(i, memo[i]))


print('---------------------------------------------------')
print('\t반복 + 메모')

memo = [0] * 11
memo[1] = 1
for i in range(2, 11):
    memo[i] = memo[i - 1] + memo[i - 2]

for i in range(1, 11):
    print('memo[{}] = {}'.format(i, memo[i]))
