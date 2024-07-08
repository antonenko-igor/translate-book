def findall(s,letter):
	L = []
	for i in range(len(s)):
		if s[i] == letter:
			L.append(i)
	return L 
print(findall("символ","в")) 