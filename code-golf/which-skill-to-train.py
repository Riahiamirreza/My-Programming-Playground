# https://codegolf.stackexchange.com/questions/267099/which-skill-to-train


x = (
    lambda skills:
        max(
            (
                (
                    (
                        lambda skills: (
                            f := lambda numbers: numbers[0] if len(numbers) == 1 else numbers[0] * f(numbers[1:])
                        )(list(pow(j, i) for i, j in enumerate(sorted(skills), start=2)))
                    )(j[0:i]+[j[i]+1]+j[i+1:]), i
                ) for i, j in enumerate([skills]*len(skills))
            ),
            key=lambda i:i[0]
        )[1]
)


assert x([3, 2, 4, 1, 2])==1
assert x([7, 19, 12, 20, 14])==3
assert x([13, 12, 19, 9, 20])==0
assert x([13, 18, 12, 12, 14])==4
assert x([18, 19, 18, 16, 13])==1
assert x([14, 14, 19, 17, 11])==2

# compact version
e=enumerate
x=lambda s:max((((lambda s:(f:=lambda n:n[0]if len(n)==1 else n[0]*f(n[1:]))([j**i for i,j in e(sorted(s),2)]))(j[:i]+[j[i]+1]+j[i+1:]),i)for i,j in e([s]*len(s))),key=lambda i:i[0])[1]

assert x([3, 2, 4, 1, 2])==1
assert x([7, 19, 12, 20, 14])==3
assert x([13, 12, 19, 9, 20])==0
assert x([13, 18, 12, 12, 14])==4
assert x([18, 19, 18, 16, 13])==1
assert x([14, 14, 19, 17, 11])==2
