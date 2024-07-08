def one_away(s1,s2):
	if len(s1) != len(s2):
		return False
	else:
		count = 0
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				count += 1
		if count == 1:
			return True
		else:
			return False
print(one_away("bike","hike")) 