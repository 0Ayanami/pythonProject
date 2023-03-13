from math import sqrt


def gcd(x, y):
    (x, y) = (y, x) if y > x else (x, y)
    while y > 0:
        rem = x % y
        x = y
        y = rem
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp % 10 + total * 10
        temp //= 10
    return total == num


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % 1 == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input('请输入一个数'))
    if is_prime(num) and is_palindrome(num):
        print('这个数是回文素数')

