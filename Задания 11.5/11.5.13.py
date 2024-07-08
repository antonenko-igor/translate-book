L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
s = "a**a****"

d = {}

for i in range(len(s)):
	if s[i] != "*":
		d[i] = s[i]

for k in L:
	while True:
		for i in d:
			if d[i] != k[i]:
				break
		else:
			print(k)
			break
		break 



