a = [int(x) for x in input('Введіть 5 цілих чисел: ').split()]
s = 0
i = 0
while i<5:
    s += a[i]
    i += 1
print(s)