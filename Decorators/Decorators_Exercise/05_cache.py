from functools import wraps


def cache(func):
    @wraps(func)
    def wrapper(n):
        res = func(n)
        wrapper.log[n] = res
        return res

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
