""" 
В качестве образца следующий текст: Oh shoot, I thought I had the
dang problem figured out. Darn it. Oh well, it was a heck of a freakin
try.
"""
s = input("Введите текст: ")
w =["shoot", "darn", "dang","freakin", "heck"]
n = ""
for i in s:
	if i[-1:] == "," or i[-1:] == ".":
		n = n + i[:-1] + " " +i[-1:] 
	else:
		n = n  + i
s = n.split()
for i in s:
	if i.lower() in w:
		print("*"*len(i),end = " ")
	else:
		print(i, end = " ") 


     

