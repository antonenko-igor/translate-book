#The program written by Igor Antonenko

data1 = input("Введите начальную дату (мм/дд/гггг) в промежутке 1901 - 2099 - ")
data2 = input("Введите конечную дату (мм/дд/гггг) в промежутке 1901 - 2099 - ")
print()
year = [31,28,31,30,31,30,31,31,30,31,30,31]
data1_split = data1.split("/")
data2_split = data2.split("/")
month_1 = int(data1_split[0])
day_1 = int(data1_split[1])
year_1 = int(data1_split[2])
month_2 = int(data2_split[0])
day_2 = int(data2_split[1])
year_2 = int(data2_split[2])
# в том же самом году
if year_2 - year_1 == 0:
	# в том же самом месяце
	if year_1 % 4 != 0 or year_1 % 4 == 0 and month_1 == month_2 :
		days = day_2 - day_1
	# если год не високосный
	elif year_1 % 4 != 0:
		days = (year[month_1 - 1] - day_1) + year[(month_1 ):(month_2 - 1)] + day_2
	# если год високосный			
	elif year_1 % 4 == 0:
		if month_1 > 2 and month_2 > 2:
			days = (year[month_1 - 1] - day_1) + sum(year[(month_1 ):(month_2 - 1)]) + day_2
		elif month_1 == 1 and month_2 > 2:
			days = (year[month_1 - 1] - day_1) + sum(year[(month_1 ):(month_2 - 1)]) + day_2 + 1
		elif month_1 == 1 and month_2 == 2 :
			days = (year[month_1 - 1] - day_1) + day_2     
elif year_2 - year_1 >= 1:
	days_years = ((year_2 - year_1) - 1) * 365

	leap_years = 0 
	for leap in range(year_1 + 1, year_2 ):
		if leap % 4 == 0:
			leap_years += 1

	if year_1 % 4 != 0 and year_2 % 4 != 0: 
		days_year_1 = 365 - year[month_1 - 1] - day_1
		days_year_2 = sum(year[:(month_2 - 1)]) + day_2
		days = days_year_1 + days_year_2 + days_years + leap_years

	elif year_1 % 4 == 0 and year_2 % 4 != 0:
		if month_1 > 2:
			days_year_1 = 365 - sum(year[:month_1 - 1]) - day_1
		elif month_1 <= 2:
			days_year_1 = 366 - sum(year[:month_1 - 1]) - day_1                	
		days_year_1 = 366 - sum(year[:month_1 - 1]) - day_1
		days_year_2 = sum(year[:(month_2 - 1)]) + day_2
		days = days_year_1 + days_year_2 + days_years + leap_years

	elif year_1 % 4 != 0 and year_2 % 4 == 0: 
		days_year_1 = 365 - sum(year[:month_1 - 1]) - day_1
		if month_2 == 1:
			days_year_2 = sum(year[:(month_2 - 1)]) + day_2
		elif month_2 == 2:
			if day_2 <= 28:
				days_year_2 = sum(year[:(month_2 - 1)]) + day_2 
			elif day_2 == 29:
				days_year_2 = sum(year[:(month_2 - 1)]) + day_2  
		elif month_2 > 2:
			days_year_2 = sum(year[:(month_2 - 1)]) + day_2 + 1
			
		days = days_year_1 + days_year_2 + days_years + leap_years

	elif  year_1 % 4 == 0 and year_2 % 4 == 0: 
	    if month_1 > 2:
	    	days_year_1 = 365 - sum(year[:month_1 - 1]) - day_1
	    elif month_1 <= 2:
	    	days_year_1 = 366 - sum(year[:month_1 - 1]) - day_1
	    if month_2 == 1:
	    	days_year_2 = sum(year[:(month_2 - 1)]) + day_2

	    elif month_2 == 2:
	    	if day_2 <= 28:
	    		days_year_2 = sum(year[:(month_2 - 1)]) + day_2
	    	elif day_2 == 29:
	    		days_year_2 = sum(year[:(month_2 - 1)]) + day_2
	    elif month_2 > 2:
	    	days_year_2 = sum(year[:(month_2 - 1)]) + day_2 + 1
	    days = days_year_1 + days_year_2 + days_years + leap_years

			
print(days,"- дней")

