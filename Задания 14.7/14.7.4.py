class Time:
	def __init__(self,time):
		self.time = time 

	def convert_to_minutes(self):
		return f"{self.time // 60}:{self.time % 60}"		

	def convert_to_hours(self):
		h = self.time // 3600
		m = self.time % 3600 // 60
		s =self.time % 3600 % 60
		return f"{h}:{m}:{s}"

t = Time(83540)
print(t.convert_to_minutes())
print(t.convert_to_hours()) 