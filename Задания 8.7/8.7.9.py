from random import sample

Questions = ["Столица Российской Федерации? ",
             "Какой штат в США имеет только одного соседа? ",
             'Первый человек в космосе? ',
             'Драгоценный металл желтого цвета? ',
             'Второй город по значению в России? ',
             'Река разделяющая Орск на Европу и Азию? ',
             'Столица США? ',
             'Полюс холода в России? ',
             'Название денежной единицы России? ',
             'Столица Франции? ']
Answers = ['Москва',
           'Мэн',
           'Гагарин',  
           'Золото',
           'Санкт-Петербург',
           'Урал',
           'Вашингтон',
           'Оймякон',
           'Рубль',
           'Париж']

c = 0
L = []
s =sample(Questions,4)
for j in range(len(s)):
    x = Questions.index(s[j])
    L.append(Answers[x])
for i in range(len(s)):
    answer = input(s[i])
    if answer == L[i]:
        c = с + 1
        print("Правильно")
    else:
        print("Неправильно")
print("Правильных ответов:  ",c)  