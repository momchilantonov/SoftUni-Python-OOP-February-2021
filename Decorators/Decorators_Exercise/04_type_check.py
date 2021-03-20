from functools import wraps


def type_check(type):
    def decorator(func):
        @wraps(type)
        def wrapper(t):
            if isinstance(t, type):
                return func(t)
            return "Bad Type"
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
