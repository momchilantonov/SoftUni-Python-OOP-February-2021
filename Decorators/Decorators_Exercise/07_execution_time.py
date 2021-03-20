from functools import wraps
import time
# from time import time


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        # start = time()
        func(*args, **kwargs)
        end = time.time()
        # end = time()
        total_time = end-start
        return total_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
