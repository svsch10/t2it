'''fizzbuzz для 20 комплектів по три числа, які записані в файл.
З файлу читається перший рядок з трьома числами, беруться з нього числа,
обчислюється fizzbuzz, результат виводиться у інший файл і т.д. до кінця
першого файла'''
import random
f_task = open('fizzbuzz_task.txt', 'w')
for i in range(20):
    for i in range(3):
        f_task.write(str(random.randint(1,50))+' ')
    f_task.write(''+'\n')
f_task.close()
f_task = open('fizzbuzz_task.txt', 'r')
f_ans = open('fizzbuzz_answer.txt', 'w')
for i in range(20):
    lines = [int(x) for x in f_task.readline().split()]
    lines.sort()
    fizz,buzz,does = lines
    f_ans.write(str(fizz)+','+str(buzz)+','+str(does)+'\n')
    for i in range(1, does+1):
        if (not i%fizz) and (not i%buzz):
            f_ans.write(''.join('FB'+' '))
        elif not i%fizz:
            f_ans.write(''.join('F'+' '))
        elif not i%buzz:
            f_ans.write(''.join('B'+' '))
        else:
            f_ans.write(''.join(str(i)+' '))
    f_ans.write(''.join('\n\n'))
f_task.close()
f_ans.close()
print('Done!')