from random import randint

L= []
for i in range(20):
	L.append(randint(1,100))

c = 0
for i in L:
	if i % 2 == 0:
		c = c + 1
print(L)
print("Количество четных чисел равно ",c) 