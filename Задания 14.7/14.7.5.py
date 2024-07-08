class Wordplay:
	def __init__(self, words):
		self.words = words

	def words_with_length(self, length):
		return [w for w in self.words if len(w) == length]

	def starts_with(self, s):
		return [w for w in self.words if w[0] == s]

	def ends_with(self, s):
		return [w for w in self.words if w[-1] == s]

	def palindromes(self):
		return [w for w in self.words if w[:] == w[: : -1]]

	def only(self, L1):
		M = []
		for w in self.words:
			flag = 0
			for i in L1:
				if i not in w:
					flag = 1
			if flag == 0:
				M.append(w)
		return M 

	def avoids(self, L2):
		M = []
		for w in self.words:
			flag = 0
			for i in L2:
				if i in w:
					flag = 1
			if flag == 0:
				M.append(w)
		return M 
        


words = [line.strip() for line in open('wordlist.txt')]
L1 = ["a","t","s","n","z","w"]
L2 = ["a","t","s","n", "z","w","f","m","y","b","d","c","r","p","o","e","q","h"]

word = Wordplay(words)
print(word.words_with_length(19))
print()
print(word.starts_with("z"))
print()
print(word.ends_with("z"))
print()
print(word.palindromes())
print()
print(word.only(L1))
print()
print(word.avoids(L2))


