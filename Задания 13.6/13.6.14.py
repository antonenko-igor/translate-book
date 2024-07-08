def is_sorted(L):
	M = L[:]
	L.sort()
	if L == M:
		return "True"
	else:
		return "False"

print(is_sorted([1,8,3,4,5])) 