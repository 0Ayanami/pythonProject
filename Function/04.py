from functools import wraps
import time


class Record(object):
    """通过定义类的方式定义装饰器"""

    def __init__(self, output):
        self.output = output
# __init__定义了装饰器的参数
# __call__会在调用Timeit对象的方法时触发

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time.time() - start)
            return result

        return wrapper


@Record(print)
def hello():
    time.sleep(1)
    print('hello')


hello()
# 由于对带装饰功能的函数添加了@wraps装饰器，可以通过func.__wrapped__方式获得被装饰之前的函数或类来取消装饰器的作用。
