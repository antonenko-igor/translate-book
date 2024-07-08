f = open("students2.txt", "w")
lines = [line.strip() for line in open("students.txt")]
#print(lines)

for line in lines:
	L = line.split("\t")
	a = L[0].split(" ")
	print(a[0][0].upper() + a[0][1:]," ",a[1][0].upper() + a[1][1:],\
		  " ",L[1]," ","301-" + L[2],file = f)
f.close()

s = open("students2.txt").read()
print(s) 
