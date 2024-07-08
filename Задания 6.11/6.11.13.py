string_1 = input("Введите первую строку:  ")
string_2 = input("Введите вторую строку той же длины: ")
string = ""

if len(string_1) != len(string_2):
	print("Строки разной длины.")
else:
	for i in range(len(string_1)):
		string = string_1[i] + string_2[i]
		print(string,end = "") 