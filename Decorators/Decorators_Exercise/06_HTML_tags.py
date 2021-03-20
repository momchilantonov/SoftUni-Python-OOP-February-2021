from functools import wraps


def tags(tag):
    def decorator(func):
        @wraps(tag)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"<{tag}>{res}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
