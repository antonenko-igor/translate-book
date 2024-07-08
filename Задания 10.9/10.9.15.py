from math import factorial
f = factorial(1000)
n = str(f)
count = 0
for i in n[::-1]:
        if i == "0":
                count += 1
        else:
                break
print("Количество нулей равно ", count) 