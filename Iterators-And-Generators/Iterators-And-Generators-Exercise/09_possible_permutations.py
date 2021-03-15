from itertools import permutations


def possible_permutations(my_list):
    perm = permutations(my_list)
    for p in perm:
        yield [*p]


[print(n) for n in possible_permutations([1, 2, 3])]
