class Circle(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        """可以像其他对象一样被传递到方法中"""
        self.x = x
        self.y = y


a = Circle(10, 20)	 # __init__
print(a.x, a.y)	 # 10 20

a(100, 200)	 # 此时a这个对象可以当做一个方法来执行，这是__call__魔法方法的功劳
print(a.x, a.y)	 # 100 200
