string = input("Введите слово(русский):  ")
x = " "

for i in string:
	if i in "аеёиоуюэыя":
	    x = x + i 
print("В слове содержатся следующие гласные -",x)  