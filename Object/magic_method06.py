class g(float):
    """千克转克当我们需要继承内置类时，例如，想要继承 int、str、tuple，
    就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据"""

    def __new__(cls, kg):
        return float.__new__(cls, kg * 1000)


a = g(50)  # 50千克转为克
print(a)  # 50000
print(a + 10000)  # 60000 由于继承了float，所以可以直接运算，非常方便！
