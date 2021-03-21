# from functools import wraps


class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            res = self.func(*args, **kwargs)
            file.write(f"Function '{self.func.__name__}' was called. Result: {res}\n")


# def store_results(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         with open("results.txt", "a") as file:
#             res = func(*args, **kwargs)
#             file.write(f"Function '{func.__name__}' was called. Result: {res}\n")
#
#     return wrapper


@store_results
def add(a, b):
    return a+b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
