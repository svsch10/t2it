#Банкомат видає суму максимально можливими купюрами
kup = [1000, 500, 200, 100, 50, 20, 10]
suma = int(input('Введіть суму грошей: '))
if suma%10 != 0:
    print('Сума повинна бути круглим числом')
else:
    for item in kup:
        k = suma//item
        if k > 0:
            print(str(k)+'x'+str(item))
        suma = suma%item