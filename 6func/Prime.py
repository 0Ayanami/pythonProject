from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for j in range(1,101):
    if is_prime(j):
        print('%d是质数' % j)
