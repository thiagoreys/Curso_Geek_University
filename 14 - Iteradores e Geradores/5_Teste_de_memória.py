# Testando a memória dos Generators

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(a)
        a, b = b, a+b
    return nums

# for n in fib_list(10000):
#     print(n)


def fib_gen(max):
    a, b = 0, 1
    for c in range(max):
        yield a
        a, b = b, a+b

# print(fib_gen(100))
# for n in fib_gen(10000):
#     print(n)


import sys

print(sys.getsizeof(fib_list(10000)))  # Tamanho em bytes
print(sys.getsizeof(fib_gen(10000)))