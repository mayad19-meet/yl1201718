from turtle import *
import random
colormode(255)
class Rectangle(Turtle):
	def __init__(self,width,hight):
		Turtle.__init__(self)
		self.width=width
		self.hight=hight
		register_shape('Rectangle',((0,self.hight),(self.width,self.hight),(self.width,0),(0,0)))
		self.shape('Rectangle')
		self.setheading(90)
	

class Square(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)
		#self.shape("square")		#self.shapesize(size)
	#def random_color(self):
		#r=random.randint(0,225)
		#g=random.randint(0,225)
		#b=random.randint(0,225)
		#self.color(r,g,b)

#s=Square(10)
#s.random_color()
R=Square(200)
#R=Rectangle(100,200)
mainloop()
