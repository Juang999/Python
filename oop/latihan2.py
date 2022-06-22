# class Hero:
# 	jumlah = 0

# 	def __init__(self, name, health, power, defense):
# 		self.name = name
# 		self.health = health
# 		self.power = power
# 		self.defense = defense
# 		Hero.jumlah += 1
	# void function, method without return
	# def siapa(self):
	# 	print("hello, my name ", self.name)

	# method with argument
	# def healthUp(self, up):
	# 	self.health += up

	# method with return
# 	def getHealth(self):
# 		return self.health

# hero1 = Hero("kai", 100, 15, 5)
# hero2 = Hero("benedetta", 100, 25, 3)

# hero1.siapa()
# hero1.healthUp(15)

# print(hero1.getHealth())

# dic = {}

# name = str(input("masukkan nama: "))
# dic["name"] = name

class Bio:
	biodata = {}

	def hello(self, name, address, age, favorit_food, hobby):
		Bio.biodata["name"] = name
		Bio.biodata["address"] = address
		Bio.biodata["age"] = age
		Bio.biodata["favorit food"] = favorit_food
		Bio.biodata["hobby"] = hobby

	def say(self):
		return Bio.biodata

biodata = Bio()

name = str(input("masukkan nama: "))
address = str(input("masukkan alamat: "))
age = int(input("masukkan umut: "))
favorit_food = str(input("masukkan favorit food: "))
hobby = str(input("masukkan hobby: "))

biodata.hello(name, address, age, favorit_food, hobby)

details = biodata.biodata

print(details)

# for detail in details:
# 	print("hello ", detail.name)
# 	print("you r from ", detail.address)
# 	print('how old r you?, ', detial.age)
# 	print("your favorit_food",detail.favorit_food)
# 	print("hobby: ", detail.hobby)