#Банкомат видає суму дрібними купюрами, але не більше 10 штук кожної дрібної купюри
kup = [10, 20, 50, 100, 200, 500, 1000]
print('Вітаємо Вас у нашому бандерівському банкоматі!')
suma = int(input('Введіть Вашу суму грошей: '))
if suma == 0:
    print('Вашу суму неможливо видати!')
else:
    print('Вашу суму можна видати таким чином:')
    for item in kup:
        if suma >= item:
            k = suma//item
            if k > 10:
                print('10x'+str(item))
                suma -= 10*item
            else:
                print(str(k)+'x'+str(item))
                suma -= k*item
    if suma != 0:
        print(str(suma)+' грн за умовами нашого банкомату видати неможливо.')
        print('Їх можна перерахувати на потреби ЗСУ.')
        m = input('Ви згодні (y/n)? ')
        while m != 'y' or m != 'n':
            if m == 'y':
                print('Дякуємо за співпрацю!')
                break
            elif m == 'n':
                print('Уході, москаль нєкрасівий!')
                break
            else:
                m = input('Якщо згодні, введіть "y", якщо ні - "n": ')
print('Слава Україні!')