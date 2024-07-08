# Antonenko Igor
name = input("Введите полное имя(ФИО) прописными буквами :")
n =  name[0].upper()
for i in range(1, len(name)):
	if  name[i-1] != " ":
		n = n + name[i]		
	else:
		n = n + name[i].upper()	
print(n) 


