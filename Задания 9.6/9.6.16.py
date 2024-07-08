from random import choice,shuffle
characters = [" 5 "," # "," A "," ! "," 0 "," b "," $ "," z ",
             " x "," - "," + "," c "," & "]*2
shuffle(characters)
list_characters = []
for i in range(5):
    M = []
    for j in range(5):
        x = choice(characters)
        M.append(x)
        characters.remove(x)
    list_characters.append(M)
print(list_characters)
list_asteriks = [[" * " for _ in range(5)] for _ in range(5)]
for row in list_asteriks:
    print("   ".join(row))
count = 0
c = 0
print("Для завершения нажмите - 10")
print()
while True :   
    row_1 = int(input("Введите координату строки - "))
    if row_1 == 10:
        break
    col_1 = int(input("Введите координату колонки - ")) 
    list_asteriks[row_1-1][col_1-1] = list_characters[row_1-1][col_1-1]   
    for row in list_asteriks:
        print("  ".join(row))
    row_2 = int(input("Введите координату строки - "))
    col_2 = int(input("Введите координату колонки - "))
    list_asteriks[row_2-1][col_2-1] = list_characters[row_2-1][col_2-1]
    for row in list_asteriks:
        print("  ".join(row))
    if list_asteriks[row_1-1][col_1-1] == list_asteriks[row_2-1][col_2-1]:
        list_characters[row_1-1][col_1-1] = " * "
        list_characters[row_2-1][col_2-1] = " * "
        list_asteriks[row_1-1][col_1-1] = " * "
        list_asteriks[row_2-1][col_2-1] = " * "
        count = count + 1
        print("Угадали!")
        print()
    else:
        list_asteriks[row_1-1][col_1-1] = " * "
        list_asteriks[row_2-1][col_2-1] = " * "
        print("Неугадали.")
        print()
    for row in list_characters:
        c = c + row.count(" * ")
    if c == 24:
        break
print("Игра закончена.")
print("Количество правильных угадываний - ", count) 