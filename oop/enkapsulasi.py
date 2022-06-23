class Hero:
	def __init__(self, name, health, attackPower):
		self.__name = name
		self.__health = health
		self.__attackPower = attackPower

	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	def serang(self, power):
		self.__health -= power

earthShaker = Hero("earthShaker", 50, 5)
print(earthShaker.getName())
print(earthShaker.getHealth())
earthShaker.serang(6)
print(earthShaker.getHealth())

