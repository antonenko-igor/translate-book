def base_20(num):
	d = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",\
	     11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T"}
	if num < 20:
		return d[num]
	elif 20 <= num <= 399:
		return (d[num//20] + d[num%20])
	elif num > 399:
		return d[num//20//20] + d[num//20//20//20] + d[num%100]

print(base_20(41)) 


