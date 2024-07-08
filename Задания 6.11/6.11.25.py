# example 3(y + 5xy - (7y + xyz))

exp = input("Введите выражение:  ")
n = ""
for i in range(len(exp)):
	if  exp[i].isdigit() and exp[i+1] =="(" or exp[i].isdigit() and exp[i+1].isalpha() :
		n = n  + exp[i] + "*"
	elif exp[i].isalpha() and exp[i+1].isalpha():
		n = n  + exp[i] + "*"
	else:
		n = n + exp[i]
print(n)    