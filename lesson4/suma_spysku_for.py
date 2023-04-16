#Обчислення суми елементів списку за допомогою циклу for
a = [int(x) for x in input('Введіть 5 цілих чисел через пропуск: ').split()]
s = 0
for item in a:
    s += item
print(s)