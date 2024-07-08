from random import choice
M = ["О","Р"]
s = "ООРРО"
L = []
for _ in range(100):
	count = 0
	sequence = ""
	while True:
		count += 1
		coin_flip = choice(M)
		sequence += coin_flip
		if len(sequence) >= 5:
			if sequence[-5:] == s:
				L.append(count)
				break
print("Среднее число бросков монеты для выпадения комбинации ООРРО при 100 "
	  "случаях равно ", sum(L)/100) 

	