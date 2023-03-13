def func(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


m = int(input('m='))
n = int(input('n='))
print(func(m) // func(n) // func(m-n))
