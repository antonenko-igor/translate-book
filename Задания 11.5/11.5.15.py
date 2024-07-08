print("Eastern - 1,", "Central - 2,", "Mountain - 3,", "Pacific - 4,")
time = input("Время:  ")
start = input("Начальная зона:  ")
end = input("Конечная зона:  ")

d = {"1": 0,"2": 1,"3": 2,"4": 3}
s = time.split(":")

if d[start] > d[end]:
	h = (int(s[0]) + d[start]) % 12
	if (int(s[0]) + d[start]) > 12:
		print(str(h),":",s[1][:2]+"am")
	else:
		print(str(h),":",s[1][:2],"pm")

	
else:
	h = (int(s[0]) - d[end]) % 12
	print(str(h),":",s[1][:2]) 
	
