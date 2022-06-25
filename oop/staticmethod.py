class Hero:
	__jumlah = 0

	def __init__(self, name):
		self.__name = name
		__jumlah += 1

	def getJumlah(self):
		return Hero.__jumlah

sniper = Hero("sniper")
rikimaru = Hero("rikimaru")
drawranger = Hero("drawranger")