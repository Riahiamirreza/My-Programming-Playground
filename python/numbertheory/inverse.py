
def inverse(a: int, prime: int) -> int:
    field: list = [i for i in range(prime)]
    for i in field:
        if (a * i)%prime == 1:
            return i
    raise ValueError

