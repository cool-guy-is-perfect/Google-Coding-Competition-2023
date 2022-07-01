T = 0
class start:
	def __init__(self):
		self.input_1 = input().split(" ")
		self.input_2 = input().split(" ")
		self.M = self.input_1[1]
		self.N = self.input_1[0]
		self.check()
	def check(self):
		if len(self.input_1) > 1:
			if len(self.input_2) == int(self.N):
				self.cont()
			else:
				self.__init__()
		else:
			print("error: need two inputs")
			self.__init__()
	def cont(self):
		global T
		T += 1
		self.sum = 0
		for self.i in self.input_2:
			self.sum += int(self.i)
		self.reminder = int(self.sum) % int(self.M)
		print(f"""Case#{T}: {self.reminder}""")
		self.__init__()
app = start()
