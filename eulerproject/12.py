import itertools


def count_divisors(n: int):
    div_count = 0
    for i in range(2, int(n**(1/2))+1):
        if not n%i:
            div_count += 1
            if i**2 != n:
                div_count += 1
    return div_count + 2

def gen_triangle_number():
    counter = itertools.count(start=1, step=1)
    sum = 0
    for i in counter:
        yield (sum := sum + i)



if __name__ == '__main__':
    gen = gen_triangle_number()
    
    while count_divisors(number := next(gen)) < 500: ...

    print(number)