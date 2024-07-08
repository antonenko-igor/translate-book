def change_case(s):
	string = ""
	for i in s:
		if i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
			string += i.lower()
		elif i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
			string += i.upper()
	return string

print(change_case("ПиТоН")) 

