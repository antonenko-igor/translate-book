lines = [line.strip() for line in open('high_temperatures.txt')]

largest = 0
values = []
for i in range(len(lines)):
    date, temp = lines[i].split(' ')
    date30, temp30 = lines[(i-30)%365].split(' ')
    diff = int(temp) - int(temp30)
    if  diff > largest:
        largest = diff
        values = [date30 + ' to ' + date + '   ' + temp30 + '-' + temp]
    elif diff == largest:
        values.append(date30 + ' to ' + date + '   ' + temp30 + '-' + temp)

for x in values:
    print(x) 