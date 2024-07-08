s1 = input("Введите слово:  ")
s2 = input("Введите зашифрованное слово: ")

if len(s1) != len(s2):
	print("Не подходит!")
else:
	d = {}
	for i in range(len(s1)):
		d[s1[i]] = s2[i]
	print(d)

c = 0
for i in range(len(s1)):
	if d[s1[i]] == s2[i] and s1[i] != s2[i]:
		c += 1
if c == len(s1):
	print("Подходит")
else:
	print("Не подходит!")  

	

	

	









