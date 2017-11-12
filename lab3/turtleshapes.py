#import turtle
#turtle.pensize(1)
#turtle.speed(100)
#turtle.color("blue")

#a=20
#for i in range(18):
#	turtle.left(a)
#	turtle.forward(120)
#	turtle.left(90)

#	turtle.forward(120)
#	turtle.left(90)
	
#	turtle.forward(120)
#	turtle.left(90)
	
#	turtle.forward(120)
#	turtle.left(90)	
	
#turtle.mainloop()
#howmanysides=6
#sideslength=120
#howmanysquares=18
#degree=60
#angle=20

#for i in range(howmanysquares):
#	turtle.left(angle)
#	for i in range(howmanysides):
#		turtle.forward(sideslength)
#		turtle.left(degree)
#turtle.mainloop()		

#for i in range(5):
#	if i==1:
#		turtle.color("blue")
#	if i==2:
#		turtle.color("green")
#	if i==3:
#		turtle.color("yellow")
#	if i==4:
#		turtle.color("pink")
#	if i==5:
#		turtle.color("red")	
				
#	turtle.forward(100)
#	turtle.right(144)

#turtle.mainloop()	


#turtle.right(90)
#turtle.forward(50)
#turtle.right(60)
#turtle.forward(50)
#turtle.right(60)
#turtle.forward(50)
#turtle.right(60)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(85)


#turtle.mainloop()

#angle=5
#for i in range(122):

#	turtle.forward(60)
#	turtle.right(60)
#	turtle.forward(30)
#	turtle.right(90)
#	turtle.forward(15)
#	turtle.home()
#	turtle.right(angle)
#	angle=angle+4

#turtle.mainloop()


class animal(object):
	def _init_(self,sound,name,age,favprite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print('yummy!!'+ self.name +'is eating'+ food)
	def description(self):
		print(self.name + 'is' +self.age +"years old and love the color"+self.favorite_color)
	def make_sound(self,time):
		print()









