import pickle
"""Python 提供了序列化模块 pickle，当使用这个模块序列化一个实例化对象时，也可以通过魔法方法来实现自己的逻辑"""


class Person(object):

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday
    """
    当调用 pickle.dumps(person) 时,__getstate__ 方法就会被调用
    在这里忽略了 Person 对象的 age 属性
    那么 person 在序列化时，就只会对其他两个属性进行保存。
    """
    def __getstate__(self):
        # 执行 pick.dumps 时 忽略 age 属性
        return {
            'name': self.name,
            'birthday': self.birthday
        }
    """
    同样地，当调用 pickle.loads(pickled_person) 时，
    __setstate__ 会被调用，其中传入的参数就是 __getstate__ 返回的结果
    """
    def __setstate__(self, state):
        # 执行 pick.loads 时 忽略 age 属性
        self.name = state['name']
        self.birthday = state['birthday']


person = Person('李四', 20, (2017, 2, 23))
pickled_person = pickle.dumps(person)  # 自动执行 __getstate__ 方法

p = pickle.loads(pickled_person)  # 自动执行 __setstate__ 方法
print(p.name, p.birthday)  # 李四 (2017, 2, 23)
# 由于执行 pick.loads 时 忽略 age 属性，所以下面执行回报错
print(p.age)  # AttributeError: 'Person' object has no attribute 'age'
