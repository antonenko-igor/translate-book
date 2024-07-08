from math import factorial as f

def binom(n,k):
	bin = (f(n)/(f(k)*(f(n-k))))
	return bin

print(binom(20,20)) 