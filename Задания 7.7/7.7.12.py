from random import randint
l = []
c = 0
max_count = 0

for i in range(101):
	l.append(randint(0,1))
print(l)

for j in l:
	if j == 0:
		c = c+1
	else:
		c = 0
	if c > max_count:
		max_count = c 
print(max_count) 
		
		


