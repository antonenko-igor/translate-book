credits = eval(input("Сколько зачетных единиц Вы имеете: "))
if credits <= 23:
	print("Вы freshman (первый курс).")
elif credits <= 53:
    print("Вы sophomore (второй курс).")
elif credits <= 83:
    print("Вы juniors (третий курс).")
elif credits >= 84:
    print("Вы seniours (четвертый курс).")        	
