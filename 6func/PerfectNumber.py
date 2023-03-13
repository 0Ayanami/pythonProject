i = 1
while i <= 10000:
    j = 1
    count = 0
    while j < i:
        if i % j == 0:
            count += j
        j += 1
    if count == i:
        print('%d是一个完美数' % count)
    i += 1
