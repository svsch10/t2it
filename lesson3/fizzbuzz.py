fizz = int(input('FIZZ: '))
buzz = int(input('BUZZ: '))
does = int(input('DOES: '))
for i in range(1, does+1):
    if (not i%fizz) and (not i%buzz):
        print('FB', end=' ')
    elif not i%fizz:
        print('F', end=' ')
    elif not i%buzz:
        print('B', end=' ')
    else:
        print(i, end=' ')