class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


"""每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
   返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行"""


def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


"""yield 的作用就是把一个函数变成一个 generator，
   带有 yield 的函数不再是一个普通函数，
   Python 解释器会将其视为一个 generator，
   调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象"""


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


"""生成器对象可以使用send()方法发送数据，发送的数据会成为生成器函数中通过yield表达式获得的值。
   这样，生成器就可以作为协程使用，协程简单的说就是可以相互协作的子程序"""
gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))
# 如果不传送数据，会默认值为None
