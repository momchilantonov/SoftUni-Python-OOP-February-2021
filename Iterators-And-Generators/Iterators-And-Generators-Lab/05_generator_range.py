def genrange(start, end):
    for el in range(start, end+1):
        yield el


print(list(genrange(1, 10)))
