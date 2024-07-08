print("""Пример магического квадрата  
       [[8,11,14,1],
       [13,2,7,12],
       [3,16,9, 6],
       [10,5,4,15]]""")

L = eval(input("Введите квадрат в виде списка размером 4 х 4 для проверки  "))

D1 = []
for i in range(4):
    D1.append(L[i][i])

D2 = []
for i in range(4):
     D2.append(L[3-i][0+i])

if sum(D1) == sum(D2):
     if sum(L[0]) == sum(L[1]) == sum (L[2]) == sum(L[3]):
          V = []
          for i in range(4):
               v = []
               for j in range(4):
                    v.append(L[j][i])
               V.append(v)
          if sum(V[0]) == sum(V[1]) == sum (V[2]) == sum(V[3]):
               print("Магический квадрат")
          else:
               print("Не магический квадрат!")
     else:
          print("Не магический квадрат!")
else:
     print("Не магический квадрат!") 

