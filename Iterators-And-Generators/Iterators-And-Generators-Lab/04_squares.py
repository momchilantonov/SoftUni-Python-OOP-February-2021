def squares(n):
    num = 1
    while True:
        if num > n:
            break
        yield num ** 2
        num += 1


print(list(squares(5)))
