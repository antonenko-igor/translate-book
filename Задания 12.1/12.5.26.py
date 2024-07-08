words = [line.strip() for line in open('wordlist.txt')]

user_letters = input("Введите подряд 7 букв(английский)")
possible_words = []
for word in words:
	if len(word) == 7:
		flag = 0
		for letter in word:
			if word.count(letter) != user_letters.count(letter):
				flag = 1
				break
		if flag == 0:
			possible_words.append(word)
print(possible_words)
	
		