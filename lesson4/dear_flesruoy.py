#Програма виводить рядки самої себе у зворотному порядку
f = open('dear_flesruoy.py', 'r')
lines = f.readlines()
lines.reverse()
for item in lines:
    print(item, end='')
f.close()
