# class Hero:
# 	def __init__(self, name, health, armor):
# 		self.__name = name
# 		self.__armor = armor
# 		self.__health = health
# 		# self.info = "name {}: \n\thealth: {}\n\tarmor: {}".format(self.__name, self.__health, self.__armor)

# 	@property
# 	def info(self):
# 		return "name {}: \n\thealth: {}\n\tarmor: {}".format(self.__name, self.__health, self.__armor)
	

# sniper = Hero('sniper', 100, 10)
# print(sniper.info)
# print(sniper.__dict__)

class Knight:
	def __init__(self, name, armor, health):
		self.__name = name
		self.__armor = armor
		self.__health = health

	@property
	def name(self):
		pass

	@name.getter
	def name(self):
		return self.__name

	@name.setter
	def name(self,input):
		self.__name = input

knight1 = Knight("Dark Knight", 15, 100)
print(knight1.__dict__)
print(knight1.name)
print("==nama ganti==")
knight1.name = "Light knight"
print(knight1.name)
print(knight1._Knight__health)