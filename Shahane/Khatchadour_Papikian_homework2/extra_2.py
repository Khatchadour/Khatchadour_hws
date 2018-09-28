n = int(input('input a number to compute the factorial: '))

for i in range(n+1):
    if i == 0:
        factorial = 1
    else:
        factorial *= i
print('%s! = %s' % (i, factorial))