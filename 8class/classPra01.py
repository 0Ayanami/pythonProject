class FootballPlayer(object):
    def __init__(self, name, number):
        self._name = name  # 单下划线表示变量是保护的但仍可以修改
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def information(self, position):
        print('%s的号码是%d，踢%s位置' % (self._name, self._number, position))

    @staticmethod
    def is_valid(number):
        return 0 <= number < 100


def main():
    if FootballPlayer.is_valid(25):
        st = FootballPlayer('muller', 25)
        st.number = 13
        st.information('前锋')
    else:
        print('球员号码不存在')


if __name__ == '__main__':
    main()
