from timeit import timeit

def loop(n=100_000_000):
    s = 0
    for i in range(n):
        s+=i
    return s
print(timeit(loop, number=1))