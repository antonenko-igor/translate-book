d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
   {'name':'Princess', 'phone':'555-3141', 'email':''},
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for k in d:
	if k["phone"][-1::] == str(8):
		print(k["name"],"- ", k["phone"]) 
	
		
	



	