class Kelas:
	def _changeName(self,gantiName):
		self.name = gantiName

kelas1 = Kelas()

kelas1._changeName("juang")

print(kelas1.__dict__);