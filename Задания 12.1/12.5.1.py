f = open("scores2.txt", "w")
lines = [line.strip() for line in open("class_scores.txt")]
#print(lines)

for line in lines:
	L = line.split(" ")
	print(L[0]," ",int(L[1]) + 5,file = f)
f.close()

s = open("scores2.txt").read()
print(s) 

	
	