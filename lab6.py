from turlte import *
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(7,"blue",10)
ball2 =	Ball(5,"green",10)

def check_collision(ball1,ball2):
	x1 = ball1.xcore()
	y1 = ball1.ycore()
	x2 = ball2.xcore()
	y2 = ball2.ycore()

    dx = math.pow(x2-x1,2)
	dy = math.pow(y2-y1,2)

	d=dx+dy
	if ball.shapesize()[0]+ball2.shapesize()[0]> d:
		ball1.color("black")
		ball2.color("red")

check_collision(ball1,ball2)
mainloop()		