from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))

print(L)
print("Среднее значение элементов списка ",sum(L)/len(L))	