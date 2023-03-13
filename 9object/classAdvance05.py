from abc import ABCMeta, abstractmethod
#  通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果


class Pet(object, metaclass=ABCMeta):
    """宠物"""
#  我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    # 上述代码子类是约定俗称的实现这个方法，加上@abc.abstractmethod装饰器后严格控制子类必须实现这个方法
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
