string = input("Введите строку:   ")

string_new = ""
for i in range(len(string)):
	if i != 1:
		string_new = string_new + string[i]
	else:
		string_new = string_new + "*"
print(string_new + "!!!") 