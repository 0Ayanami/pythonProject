class Person(object):
    """构造器，当一个实例被创建的时候调用的初始化方法。"""
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    """当调用 bool(obj) 时，会调用 __bool__() 方法，返回 True 或 False"""
    def __bool__(self):
        return self.age > 18

    def __setattr__(self, key, value):
        """定义当一个属性被设置时的行为"""
        if key not in ('name', 'age', 'uid'):
            return
        if key == 'age' and value < 0:
            raise ValueError()
        super(Person, self).__setattr__(key, value)

    def __getattr__(self, key):
        """定义当用户试图获取一个不存在的属性时的行为"""
        return 'unknown'

    def __delattr__(self, key):
        """删除某个属性"""
        if key == 'name':
            raise AttributeError()
        super().__delattr__(key)

    def __getattribute__(self, key):
        """所有属性/方法调用都经过这里"""
        if key == 'money':
            return 100
        elif key == 'hello':
            return self.say
        return super().__getattribute__(key)

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        """对象 != 判断"""
        return self.name != other.name

    def __lt__(self, other):
        """对象 < 判断 根据self.age"""
        return self.age < other

    def __gt__(self, other):
        """对象 > 判断 根据self.age"""
        return self.age > other


p1 = Person()
p1.age = 17  # 调用__setattr__
p1.name = '张三'  # 调用__setattr__
p2 = Person()
setattr(p2, 'name', '李四')
setattr(p2, 'age', 19)
p3 = Person()
setattr(p3, 'name', '王五')
setattr(p3, 'age', 8)
print(bool(p1))  # False
print(bool(p2))  # True
print(p1.sex)  # unknown
print(p1 == p2)  # False
print(p2 != p3)  # True
print(p1 < p3)  # False
print(p1 > p2)  # False
# 上面只要是访问属性的地方，都会调用__getattribute__方法
