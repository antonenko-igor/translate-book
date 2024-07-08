string = input("Введите строку для дешифрования: ")
decrypted = ""
for i in range(3):
    for j in range(i,14,5):
        decrypted += string[j]
print(decrypted) 