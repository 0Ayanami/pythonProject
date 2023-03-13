from functools import wraps
import time


def record_time(func):
    """自定义装饰函数的装饰器"""

    # 使用 wraps 装饰内部方法wrapper
    # 被装饰的方法，除了增加额外的功能之外，方法的属性信息依旧可以保留原来的
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)# 传递参数给真实调用的方法
        print(f'{func.__name__}: {time.time() - start}秒')
        return result

    return wrapper


@record_time
def hello(fname, lname):
    time.sleep(1)
    print('hello,%s.%s' % (fname, lname))


hello('Thomas', 'Muller')
