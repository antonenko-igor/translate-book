m = input("Введите строку для шифрования:  ")

m1 = ""
m2 = ""

for i in range(len(m)):
	if i % 2 == 0:
		m1 = m1 + m[i]
	else:
		m2 = m2 + m[i]
print(m1 + m2) 