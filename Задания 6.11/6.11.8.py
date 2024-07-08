amount = eval(input("Введите количество email адресов:  "))

nSt = 0
nPr = 0

for i in range(amount):
	y = input("Введите email: - ")
	if y[-20:] == "@student.college.edu":
		nSt = nSt + 1
	if y[-17:] == "@prof.college.edu":
		nPr = nPr + 1
print("количество адресов студентов =  ",nSt, 
	  "количество адресов профессоров = ",nPr ) 