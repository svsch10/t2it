#https://www.nytimes.com/live/2023/05/10/world/russia-ukraine-news
#----------Отримуємо текст для обробки------------------------------------------
f_task = open('words_input.txt', 'r')
words = []
for line in f_task:
    words.extend(line.split())
f_task.close()
#----------Очищуємо список від непотрібних символів-----------------------------
trash = ['“', '”', ',', '.', ';', '—', ':'] #список символів, які слід видалити
n = len(words)
for i in range(n): #очищення списку від символів розділових знаків
    words[i] = words[i].translate({ord(j): None for j in trash})
#----------Підрахунок частоти слів у тексті і виведення результатів-------------
f_ans = open('words_output.txt', 'w')
words.sort()
for word in words:
    if word == '': #видалення порожніх позицій, де колись стояли тире
        words.remove(word)
    else:
        n = words.count(word)
        f_ans.write(word + ' - ' + str(words.count(word)) + '\n')
        for i in range(n):
            words.remove(word)
f_ans.close()