class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


'''python 并没有从语法上严格保证私有属性或方法的私密性
   在实际开发中，我们并不建议将属性设置为私有的，
   所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的'''


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
