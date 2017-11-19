from turtle import *
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		def random_color(self,color):
			r=random.randit(0,225)
			g=random.randit(0,225)
			b=random.randit(0,225)
			self.color(r,g,b)