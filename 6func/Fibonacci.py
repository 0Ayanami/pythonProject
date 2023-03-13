a = 1
print('%d' % a)
b = 1
print('%d' % b)
n = 2
while n < 20:
    c = a + b
    print('%d' % c)
    a = b
    b = c
    n += 1
