days = {'Январь':31, 'Февраль':28, 'Март':31, 'Апрель':30,
'Май':31, 'Июнь':30, 'Июль':31, 'Август':31,
'Сентябрь':30, 'Октябрь':31, 'Ноябрь':30, 'Декабрь':31}
items = list(days.items())
print(items)

l = len(items)
for i in range(l-1):
	for j in range(i+1,l):
		if items[i][1]>items[j][1]:
			t = items[i]
			items[i] = items[j]
			items[j] = t 
	sortdays = dict(items)
print(sortdays) 
