a = [int(x) for x in input('Введіть 5 цілих чисел: ').split()]
s = 0
for item in a:
    s += item
print(s)