'''Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до
нижнього регістру. Друга функція прийматиме рядок та приводитиме його до
верхнього регістру'''

def Up(text):
    return text.upper()

def Low(text):
    return text.lower()

f_task = open('UpperLower_input.txt', 'r')
text = f_task.read()
f_task.close()
diskriminator = input("Оберіть регістр: верхній ('U') чи нижній ('L')? ")
if diskriminator == 'U':
    print(Up(text))
elif diskriminator == 'L':
    print(Low(text))
else:
    print('Помилка вибору!')