n = int(input('Задайте число: '))
if n<0 or not n%2:
    print('Задайте додатне непарне число!')
else:
    for i in range(1,n+1,2):
        print(int((n-i)//2)*' ' + '*'*i)
    for i in range(n-2,0,-2):
        print(int((n-i)//2)*' ' + '*'*i)