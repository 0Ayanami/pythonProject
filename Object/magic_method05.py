class Washer:
    def __int__(self):
        pass
    """
    设计的目的是不一样的： 
    1. __repr__的目标是准确性，或者说，__repr__的结果是让解释器用的
    2. __str__的目标是可读性，或者说，__str__的结果是让人看的
    """
    def __repr__(self):
        return '我是__repr__()魔法方法！'

    def __str__(self):
        """
        这个str的作用就是：类的说明或对象状态的说明
        :return:
        """
        return '我是__str__魔法方法！'

    def __del__(self):
        """
        析构器，当一个实例被销毁时自动调用的方法
        当删除对象时，解释器会自动调用del方法
        """
        print('对象已删除！')


hair = Washer()
print(hair)
# output:
# 对象已删除！
