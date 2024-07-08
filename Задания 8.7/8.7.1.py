s = input("Введите текст(на английском):  ")
s = s.lower()
c = 0
l = s.split()
for i in l:
	if i == "the" or i == "a" or i == "an":
		c = c + 1
print("Количество артиклей равно ",c)		
