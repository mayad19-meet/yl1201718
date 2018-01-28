import turtle
import time
import random
from personal_project import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HIGHT = turtle.getcanvas().winfo_width()/2
MY_BALL = Ball(0,0,10,50,100,"lightpink")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH)+int(MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HIGHT)+ int(MAXIMUM_BALL_RADIUS), int(SCREEN_HIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx == 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy == 0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(),random.random())
	ball1 = Ball(x, y, dx, dy, radius, color)
	BALLS.append(ball1)


def move_all_balls():
	for z in BALLS:
		z.move(SCREEN_WIDTH, SCREEN_HIGHT)
# 2**0.5
def collide(ball_a, ball_b):
	if ball_a == ball_b :
		return False
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	DISTANCE_BETWEEN_CENTERS = ((x1-x2)**2+(y1-y2)**2)**0.5
	if DISTANCE_BETWEEN_CENTERS+10 <= ball_a.radius + ball_b.radius:
		return True	
	else:
		return False
def check_all_balls_collidion():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				radius_a = ball_a.radius
				radius_b = ball_b.radius
				x_coordinate = random.randint(int(-SCREEN_WIDTH)+int(MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				y_coordinate = random.randint(int(-SCREEN_HIGHT)+ int(MAXIMUM_BALL_RADIUS), int(SCREEN_HIGHT) - int(MAXIMUM_BALL_RADIUS))
				x_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while x_axis_speed == 0:
					x_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				y_axis_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while y_axis_speed == 0:
					y_axis_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)


				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				r=random.randint(0,225)
				g=random.randint(0,225)
				b=random.randint(0,225)
				color=(r,g,b)
				if radius_a<radius_b:
					ball_a.goto(x_coordinate,y_coordinate)
					ball_a.dx=x_axis_speed
					ball_a.dy=y_axis_speed
					ball_a.radius=radius
					ball_a.shapesize(radius/10)
					ball_a.color(color)
					ball_b.radius=ball_b.radius+1
					ball_b.shapesize(ball_b.radius/10)
				else:
					ball_b.goto(x_coordinate,y_coordinate)
					ball_b.dx=x_axis_speed
					ball_b.dy=y_axis_speed
					ball_b.radius=radius
					ball_b.shapesize(radius/10)
					ball_b.color(color)
					ball_a.radius=ball_a.radius+1
					ball_a.shapesize(ball_a.radius/10)

def check_myball_collision():
	for i in range(len(BALLS)):
		if collide(i,MY_BALL)==True:
			if MY_BALL.radius>i.radius:
				i.goto(x_coordinate,y_coordinate)
				i.dx=x_axis_speed
				i.dy=y_axis_speed
				i.radius=radius
				i.shapesize(radius/10)
				i.color(color)
				MY_BALL.radius=MY_BALL.radius+1
				MY_BALL.shapesize(MY_BALL.radius/10)
			if MY_BALL.radius<i.radius:
				return False		

	return True

def movearound(event):
	x_coordinate=event.x-SCREEN_WIDTH 	
	y_coordinate=SCREEN_HIGHT-event.y
	MY_BALL.goto(x_coordinate,y_coordinate)
	turtle.getcanvas().bind("<Motion>",movearound)
	turtle.listen()

while RUNNING is True:
	move_all_balls()
	check_all_balls_collidion()
	turtle.getscreen().update()
turtle.mainloop()