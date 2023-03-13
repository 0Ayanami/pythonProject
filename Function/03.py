from functools import wraps
import time


def record(output):
    """可以参数化的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            output(func.__name__, time.time() - start)
            return result

        return wrapper

    return decorate


@record(print)
def hello():
    time.sleep(1)
    print('hello')


hello()
