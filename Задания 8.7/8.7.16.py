n = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

L = [(n[i+1]-n[i]) for i in range(len(n)-1)]
print(L,"max = ",max(L))
print("Количество разницы 2 в процентах: ",(L.count(2)/len(L))*100) 