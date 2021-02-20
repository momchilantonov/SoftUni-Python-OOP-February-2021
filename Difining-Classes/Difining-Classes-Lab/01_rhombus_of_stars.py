def generate_rhombus(i, n):
    indent = ' ' * (n-i-1)
    stars = '* ' * (i+1)
    return f'{indent}{stars}'


def print_rhombus(n):
    for i in range(n):
        print(generate_rhombus(i, n))
    for i in range(n-2, -1, -1):
        print(generate_rhombus(i, n))


nums = int(input())

print_rhombus(nums)
