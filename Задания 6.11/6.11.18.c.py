string = input("Введите строку:   ")
letter = input("Введите букву:    ")

index = " "
for i in range(len(string)):
	if string[i] == letter:
		index = index + str(i) #Число в строковом представлении
if index == " ":
	print("Буква в строке отсутствует")
else:
	print("Индекс первого вхождения буквы - ", index[1]) 
	
		





		



		
   
