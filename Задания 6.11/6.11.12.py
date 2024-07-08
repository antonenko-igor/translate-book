s = input("Введите слово:  ")
a = ""

for i in range(len(s)):
	if i % 2 != 0:
		a = a + s[i].upper()
	else:
		a = a + s[i]
print(a) 

