class Hero:
	__jumlah = 0

	def __init__(self, name, health, attPower, armor):
		self.__name = name
		self.__healthStandard = health
		self.__attackPowerStandard = attPower
		self.__armorStandard = armor
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthStandard * self.__level
		self.__attPower = self.__attackPowerStandard * self.__level
		self.__armor = self.__armorStandard * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{}: \n\thealth = {}/{} \n\tattack: {}\n\tarmor: {}".format(self.__name, self.__health, self.__healthMax, self.__attPower, self.__armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if (self.__exp >= 100:
			print(self.__name, ' level up')
			self.__level += 1
			self.__exp -= 100
			self.__healthMax = self.__healthStandard * self.__level
			self.__attPower = self.__attackPowerStandard * self.__level
			self.__armor = self.__armorStandard * self.__level



# name = str(input("masukkan nama hero: "))
# health = int(input("masukkan jumlah darah: "))
# attPower = int(input("masukkan nilai kekuatan: "))
# armor = int(input("masukkan nilai bertahan: "))

slardar = Hero("slardar", 100, 5, 10)
print(slardar.info)		