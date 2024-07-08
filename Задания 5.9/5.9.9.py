s = 0
for i in range(1, 1001):
	if i % round(i**(1./2), 4) != 0:
		s = s + 1
print("x^2 - ",s)
print()
c = 0
for i in range(1, 1001):
	if i % round(i**(1./3), 4) != 0:
		c = c + 1
print("x^3 - ",c)
print()
f = 0
for i in range(1, 1001):
	if i % round(i**(1./5), 4) != 0:
		f = f + 1
print("x^5 - ",f) 