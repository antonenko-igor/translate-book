from random import randint

n = 0
count = 0
while n < 1000:
	n += 1
    
	d1 = randint(1,6)
	d2 = randint(1,6)
	d3 = randint(1,6)
	d4 = randint(1,6)
	d5 = randint(1,6)
	if d1==d2==d3==d4==d5:
		count += 1
print("При имитации 10000 бросков:")
print("Число выпадения одного числа одновременно равно ", count,
      "Процент выпадения равен ","{:.1f}".format((count/1000)*100),"%")  
