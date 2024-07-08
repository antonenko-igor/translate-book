from random import randint
L = []
N = [2,3,4,5,6,7,8,9,10,11,12]
x = 10000

for i in range(x):
	dice1 = randint(1,6)
	dice2 = randint(1,6)
	L.append(dice1 + dice2)
	
for j in N:
	if j in L:
		L.count(j)
		print(j,"-", round(((L.count(j)/x)*100), 3)) 