days = {'Январь':31, 'Февраль':28, 'Март':31, 'Апрель':30,
'Май':31, 'Июнь':30, 'Июль':31, 'Август':31,
'Сентябрь':30, 'Октябрь':31, 'Ноябрь':30, 'Декабрь':31}

l = list(days.items())

m = input("Введите название месяца с заглавной(первые три буквы):  ")

for i in range(len(l)):
    if l[i][0][0:3] == m:
        print("Количество дней в месяце",l[i][0],"составляет -", l[i][1] )
   
print(l[5][0][0:3]) 


