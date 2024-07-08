s  = input("Введите римское число:  ")
n = s.upper()

d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
val = 0

for i in range(len(n)):
	if i > 0 and d[n[i]] > d[n[i - 1]]:
		val += d[n[i]] - 2*d[n[i - 1]]
	else:
		val += d[n[i]]
print(val) 