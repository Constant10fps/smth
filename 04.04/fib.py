from math import hypot
from random import randint, uniform


def fib_seq(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for _ in range(n-2):
        a, b = b, a+b
    return b

def factorial(n: int) -> int:
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c *= i
    return c

def monte_carlo_pi(n: int) -> float:
    total = 0
    for _ in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if (x ** 2 + y ** 2) <= 1:
            total += 1
    return 4 * total / n
