from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))
L.sort()
print(L)
print("Второе наибольшее значение - ",L[-2])
print("Второе наименьшее значение - ",L[1])  