"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Stuff(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight


def input_info():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    max_weight, num_of_things = map(int, input().split())
    all_stuff = []
    for _ in range(num_of_things):
        all_stuff.append(Stuff(*input_info()))
    all_stuff.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for item in all_stuff:
        if total_weight + item.weight <= max_weight:
            total_weight += item.weight
            total_price += item.price
            print(f'小偷偷了{item.name}')
    print(f'总价值为{total_price}')


if __name__ == '__main__':
    main()
