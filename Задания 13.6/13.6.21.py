def binary_search(words, word):
	start = 0
	end = len(words) - 1

	while start <= end:
		middle = (start + end)//2
		midpoint = words[middle]
		if midpoint > word:
			end = middle - 1
		elif midpoint < word:
			start = middle + 1
		else:
			return True

words = [line.strip() for line in open('wordlist.txt')]
print(binary_search(words, "queue")) 
