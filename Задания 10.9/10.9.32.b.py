from random import randint
L1 = [1,2,3,4,5]
L2 = [2,3,4,5,6]
count = 0

for i in range(10000):
	L = []
	for j in range(5):
		d = randint(1,6)
		L.append(d)
		L.sort()
		if L == L1 or L == L2:
			count += 1
		
print("Вероятность выпадения a large straight равна ",round((count/10000)*100,2), "%")
             
