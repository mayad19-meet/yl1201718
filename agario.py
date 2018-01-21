from turtle import *
import time
import random
from personal_project.py import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING = turtle
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HIGHT = turtle.getcanvas().winfo_width()/2
MY_BALL = Ball(0,0,10,50,100,"lightpink")

NUMBER_OF_BALL = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS)
	x = random.randint(int(-SCREEN_WIDTH)+int(MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HIGHT)+ int(MAXIMUM_BALL_RADIUS), int(SCREEN_HIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx = 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy = 0:

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random(),random.random())
	ball1 = Ball(self, x, y, dx, dy, radius, color)
	BALLS.append(ball1)


def move all balls():
	for z in BALLS:
		Z,move(SCREEN_WIDTH, SCREEN_HIGHT)

def collide(ball_a, ball_b):
	if ball_a = ball_b :
		return False
	DISTANCE_BETWEEN_CENTERS = int(ball_a.pos()) - int(ball_b.pos())
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
				x-coordinate = random.randint(int(-SCREEN_WIDTH)+int(MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				y-coordinate = random.randint(int(-SCREEN_HIGHT)+ int(MAXIMUM_BALL_RADIUS), int(SCREEN_HIGHT) - int(MAXIMUM_BALL_RADIUS))
				x-axis speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while x-axis speed* == 0:
					x-axis speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				y-axis speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				if dy = 0:

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random(),random.random())
	ball1 = Ball(self, x, y, dx, dy, radius, color)
	BALLS.append(ball1)


