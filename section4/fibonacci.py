# -*- coding: utf-8 -*-


import functools


def fibonacci(n: int) -> int:
    a = b = 1
    for _ in range(n-1):
        a, b = b, a+b
    return b


@functools.lru_cache()
def fibonacci2(n: int) -> int:
    if n < 2:
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)


print(fibonacci(3))
print(fibonacci(5))
print(fibonacci2(5))
print(fibonacci2(30))
print(fibonacci(100))
print(fibonacci2(100))
