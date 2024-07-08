def matches(s1,s2):
	count = 0
	if s1 < s2:
		l = len(s1)
	else:
		l = len(s2)
	for i in range(l):
		if s1[i] == s2[i]:
			count += 1
	return count

print(matches("python","path")) 