lines = [line.strip() for line in open("namelist.txt")]

initials = input("Введите инициалы(заглавные английские буквы): ")
for line in lines:
	L = line.split(" ")
	
	if len(initials) == 2:
		if len(L) == 2:
			if initials[0] == L[0][0] and initials[1] == L[1][0]:
				print(" ".join(L))
		else:

			if initials[0] == L[0][0] and initials[1] == L[2][0]:
				print(" ".join(L))

	elif len(initials) == 3:
		if len(L) == 2:
			if initials[0] == L[0][0] and initials[2] == L[1][0]:
				print(" ".join(L))
		else:
			if initials[0] == L[0][0] and initials[2] == L[2][0]:
				print(" ".join(L)) 

	




		
			
