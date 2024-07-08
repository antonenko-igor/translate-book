words = [line.strip() for line in open('wordlist.txt')]
s = input("Введите строку ")
s_l = s.lower()
L = s_l.split()
for i in L:
 	if i not in words:
 		print("Слово ",i," с ошибкой") 