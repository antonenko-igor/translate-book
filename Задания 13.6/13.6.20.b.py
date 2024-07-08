def merge(L1,L2):
	L = L1 + L2
	for j in range(len(L)-1):
		for i in range(len(L)-j-1):
			if L[i] > L[i+1]:
				L[i],L[i+1] = L[i+1],L[i]
	return L

print(merge([5,6,7,8], [1,2,3])) 