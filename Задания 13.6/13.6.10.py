def closest(L,n):
	L.sort()
	if max(L) < n:
		return max(L)
	else:
		for i in range(len(L)):
			if L[i] < n < L[i+1]:
				return L[i]
print(closest([1,6,3,9,11],18)) 