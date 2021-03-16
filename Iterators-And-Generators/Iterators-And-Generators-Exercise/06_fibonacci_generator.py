def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b


generator = fibonacci()
for i in range(5):
    print(next(generator))
