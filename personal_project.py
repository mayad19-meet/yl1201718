from turtle import *
import random
import turtle
turtle.hideturtle()
colormode(255)
screen_size = 640,480

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.penup()
		self.setposition(x,y)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius/10)

		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		self.color((r,g,b))

	def move(self,screen_width, screen_hight):
		currentx=self.xcor()
		currenty=self.ycor()
		new_x= currentx+self.dx
		new_y= currenty+self.dy
		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		top_side_ball = new_y +self.radius
		bottom_side_ball = new_y - self.radius

		self.goto(new_x , new_y)

		if right_side_ball >= screen_width:
			self.dx = -self.dx
		if left_side_ball <= -screen_width:
			self.dx = -self.dx
		if top_side_ball >= screen_hight:
			self.dy = -self.dy
		if bottom_side_ball <= -screen_hight:
			self.dy = -self.dy



