string = input("Введите строку - ")
string = string.lower()

for c in ", . ":
	string = string.replace(c," ")
print(string)  