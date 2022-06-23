class Hero:
	def __init__(self, name, health, attackPower, armor):
		self.name = name
		self.health = health
		self.attackPower = attackPower
		self.armor = armor

	def serang(self, lawan):
		print(self.name + " menyerang " + lawan.name)
		lawan.diserang(self, self.attackPower)

	def diserang(self, lawan, attactPowerLawan):
		print(self.name + " diserang "  + lawan.name)
		attack_diterima = attactPowerLawan/self.armor
		print('serangan diterima: ' + str(attack_diterima))
		self.health -= attack_diterima
		print("darah ", self.name, " tersisa: ", str(self.health))

sniper = Hero("sniper", 100, 15, 5)
rikimaru = Hero("rikimaru", 100, 5, 10)

sniper.serang(rikimaru)
