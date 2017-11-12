class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print('yummy!!'+ self.name +'is eating'+ food)
	def description(self):
		print(self.name + 'is' +self.age +"years old and love the color"+self.favorite_color)
	def make_sound(self,time):
		print(self.sound*time)
a = Animal('ploply','Tut',7,'red')
a.eat('strewberries')
a.make_sound(5)

class.person(object):
	def __init__(self,name,18,)