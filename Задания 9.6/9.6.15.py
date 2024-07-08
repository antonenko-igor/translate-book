from random import choice
C = ["Канада","Россия","Китай","Германия","Испания","Япония",
     "Индонезия","Польша","Чили"]
c = choice(C)
k = list(c)
A = []
for j in range(len(c)):
	A.append("-")
print(A)
count = 0
print("Первая буква заглавная")
while "-" in A and count < 5:	
	letter = input("Введите букву - ")
	if letter in k:
		for i in range(len(k)):
			if k[i]==letter:
				A[i]=letter
	else:
		count = count + 1
		print("Буква не найдена")
		print("Осталось попыток - ",5 - count)
	print(" ".join(A))
if count >= 5:
	print("Вы проиграли!")
	print("Слово было - ",c) 