a = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

L = []
c = 1
for i in range(len(a)):
	L.append(a[i]*c)
	c = c + 1
print(L) 