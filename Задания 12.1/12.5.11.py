word = input("Введите слово(на английском):    ")
words = [line.strip() for line in open('wordlist.txt')]
if word in words:
	print("Слово существует.")
else:
	print("Слово не существует.")  