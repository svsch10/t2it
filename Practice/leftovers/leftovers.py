f_task = open('leftovers_input.txt', 'r')
for line in f_task:
    numbers,leftovers = line.split(';')
    numbers = list(map(int, numbers.split()))
    leftovers = list(map(int, leftovers.split()))
    average = sum(numbers) // len(numbers)
    remainder = sum(numbers) % len(numbers)
    if [average, remainder] == leftovers:
        print('True')
    else:
        print('False')
f_task.close()