year = int(input('enter a year: '))

def f(year):
    return (year + 99) // 100

print('century %s is in:' % (year), f(year))