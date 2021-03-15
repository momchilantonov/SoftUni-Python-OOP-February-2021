def is_prime(num):
    if num > 1:
        for i in range(2, num // 2+1):
            if num % i == 0:
                return False
        return True
    return False


def get_primes(my_list):
    for num in my_list:
        if is_prime(num):
            yield num


print(list(get_primes([0, 2, 4, 3, 5, 6, 9, 1, 0])))


# import sympy
#
#
# def get_primes(my_list):
#     for num in my_list:
#         if sympy.isprime(num):
#             yield num
