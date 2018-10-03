s = [3, 6, -2, -5, 7, 3]

def f(s):
    product = s[0]*s[1]
    for i in range(1, len(s)-1):
        temp = s[i]*s[i+1]
        if product < temp:
            product = temp
    return product
print(f(s))





