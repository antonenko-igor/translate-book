count = 0
for i in range(1,101):
	if (i**2) % 10 == 1:
		print(i, "  ", i**2)
		count = count + 1		
print(count)	