from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))

print(L)
print("Наибольшее значение - ",max(L))
print("Наименьшее значение - ",min(L)) 