# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

for i in range(20):
    for j in range(33):
        k = 100 - i - j
        if 5 * i + j * 3 + k // 3 == 100 and k % 3 == 0:
            print('公鸡%d只，母鸡%d只，小鸡%d只。' % (i, j, k))


# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish = 6
while True:
    enough = True
    total = fish
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
            enough = True
        else:
            enough = False
            break
    if enough:
        print('至少捕了%d条鱼' % fish)
        break
    fish += 5
