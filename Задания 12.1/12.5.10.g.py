words = [line.strip() for line in open('wordlist.txt')]
ten = 0
seven = 0
for word in words:
	if len(word) == 10:
		ten += 1
	if len(word) == 7:
		seven += 1
if ten > seven:
	print("Слов из десяти букв больше, чем из семи - ", ten, ">", seven)
else:
	print("Слов из десяти букв меньше, чем из семи - ", ten, "<", seven)  
