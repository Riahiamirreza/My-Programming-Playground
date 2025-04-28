def sum_of_divisors(n: int) -> list[int]:
    sum_of_divs = 1
    for i in range(2, int(n**(1/2)) + 1):
        if not n % i:
            sum_of_divs += i
            if i*i != n:
                sum_of_divs += n//i
    return sum_of_divs


def proper_divisors(n: int) -> list[int]:
    divs = [1]
    for i in range(2, int(n**(1/2)) + 1):
        if not n % i:
            divs.append(i)
            if i*i != n:
                divs.append(n//i)
    return sum(divs)

if __name__ == '__main__':
    short = sum_of_divisors
    print(sum(i for i in range(1, 10_000) if short(short(i)) == i and short(i) != i))


