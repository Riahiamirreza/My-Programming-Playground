# https://codegolf.stackexchange.com/questions/267099/which-skill-to-train


x = (lambda skills: max((((lambda skills: (f := lambda numbers: numbers[0] if len(numbers) == 1 else numbers[0] * f(numbers[1:]))(list(pow(j, i) for i, j in enumerate(sorted(skills), start=2))))(j[0:i]+[j[i]+1]+j[i+1:]), i) for i, j in enumerate([skills]*len(skills))), key=lambda i:i[0])[1]+1)

print(
    x([3, 2, 4, 1, 2])
)
print(
    x([7, 19, 12, 20, 14])
)
print(
    x([13, 18, 12, 12, 14])
)