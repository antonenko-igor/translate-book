"""
IDLE Shell 3.11.4 отображает вывод некорректно.
Используйте py.exe
"""
n = eval(input("Введите высоту треугольника: "))
L = []
 
for i in range(0, n):
    r = ["1"] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            r[j] = str(int(L[i-1][j-1]) + int(L[i-1][j])) 
    L.append(r) 
for i in range(len(L)):
	s = " ".join(L[i])
	print("{:^100s}".format(s))
input() 