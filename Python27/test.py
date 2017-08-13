class Fab(object):
	def __init__(self, num):
		self.num = num
		a, b, L = 0, 1, [0]
		for i in range(0,self.num):
			L.append(b)
			b = a + b
			a = L[-2]
		self.L = L

	def output(self):
		for num in self.L:
			print num

myFab = Fab (5)
myFab.output()