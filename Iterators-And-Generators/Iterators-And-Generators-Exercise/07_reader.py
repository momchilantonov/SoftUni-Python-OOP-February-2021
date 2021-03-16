def read_next(*args):
    for arg in args:
        yield ''.join(str(el) for el in arg)


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
