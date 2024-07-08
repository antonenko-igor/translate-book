emails = [line.strip() for line in open('emailslist.txt')]

for email in emails:
	if "@prof.college.edu" not in email:
		print(email, end = "; ")  
	