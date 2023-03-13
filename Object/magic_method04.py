class MyList(object):
    """自己实现一个list"""

    def __init__(self, values=None):
        # 初始化自定义list
        self.values = values or []
        self._index = 0

    def __setitem__(self, key, value):
        # 添加元素,定义设置容器中指定元素的行为
        self.values[key] = value

    def __getitem__(self, key):
        # 获取元素,定义获取容器中指定元素的行为
        return self.values[key]

    def __delitem__(self, key):
        # 删除元素,定义删除容器中指定元素的行为
        del self.values[key]

    def __len__(self):
        # 自定义list的元素个数,定义当被 len() 调用时的行为
        return len(self.values)

    def __iter__(self):
        # 可迭代,定义当迭代容器中的元素的行为
        return self
    """
       1）返回 iter(obj)：代表使用 obj 对象的迭代协议，一般 obj 是内置的容器对象；
       2）返回 self：代表迭代的逻辑由本类来实现，此时需要重写 next 方法，实现自定义的迭代逻辑
          在这个例子中，__iter__ 返回的是 self，所以需要定义 __next__ 方法，实现自己的迭代细节
          __next__ 方法使用一个索引变量，用于记录当前迭代的位置
          这个方法每次被调用时，都会返回一个元素
          当所有元素都迭代完成后，此时 for 会停止迭代
          若迭代时下标超出边界，这个方法会返回 StopIteration 异常
    """
    def __next__(self):
        # 迭代的具体细节
        # 如果__iter__返回self 则必须实现此方法
        if self._index >= len(self.values):
            raise StopIteration()
        value = self.values[self._index]
        self._index += 1
        return value

    def __contains__(self, key):
        # 元素是否在自定义list中,定义当使用成员测试运算符（in 或 not in）时的行为
        return key in self.values

    def __reversed__(self):
        # 反转,定义当被 reversed() 调用时的行为
        return list(reversed(self.values))
# 初始化自定义list


my_list = MyList([1, 2, 3, 4, 5])
print(my_list[0])	     # __getitem__
my_list[1] = 20		     # __setitem__

print(1 in my_list)	     # __contains__
print(len(my_list))     # __len__

print([i for i in my_list])  # __iter__
del my_list[0]	             # __del__

reversed_list = reversed(my_list)  # __reversed__
print([i for i in reversed_list])  # __iter__
