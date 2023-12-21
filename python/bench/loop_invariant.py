import timeit


def before():
    values = (1, 2, 3, 4, 5, 6)
    x = 54
    for i in range(10_000):
        _ = (len(values) * x) + i


def after():
    values = (1, 2, 3, 4, 5, 6)
    x = 54
    y = len(values) * x
    for i in range(10_000):
        _ = y + i

print(timeit.timeit(before, number=100))
print(timeit.timeit(after, number=100))
