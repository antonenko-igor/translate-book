print("inches - дюймы\nfeet - футы\nyards - ярды\nmiles - мили\nkilometrs - километры")
print("meters - метры\ncentimetrs - сантиметры\nmillimetrs - миллиметры")

class Converter:
	def __init__(self,length,unit):
		self.length = length
		self.unit = unit

	def transform(self, unit_transform):
		unit_list = ["дюймы","футы","ярды","мили","километры","метры","сантиметры",
		            "миллиметры"]
		value_in_foot = [12,1,1/3,1/5280,1/3281,1/3.281,1/30.48,1/304.8]
		if unit_transform in unit_list:
			length_transform = round(self.length*value_in_foot[unit_list.index(
				                     unit_transform)]/value_in_foot
				                     [unit_list.index(self.unit)], 6)
		return f"{length_transform} {unit_transform}"

	def inches(self):
		return self.transform("дюймы")

	def feet(self):
		return self.transform("футы")

	def yards(self):
		return self.transform("ярды")

	def miles(self):
		return self.transform("мили")

	def kilometrs(self):
		return self.transform("километры")

	def meter(self):
		return self.transform("метры")

	def centimetrs(self):
		return self.transform("сантиметры")

	def millimetrs(self):
		return self.transform("миллиметры")
c = Converter(9,"дюймы")
print(c.inches())
print(c.feet())
print(c.millimetrs()) 

