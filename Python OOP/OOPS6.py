class Parrot:

	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot can't swim")

class Penguin:

	def fly(self):
		print("Penguin can't fly")

	def swim(self):
		print("Penguin can swim")

# common interface

def flying_test(bird):
	bird.fly()

# instantiate objects

blu = Parrot()
peggy = Penguin()

# Passing the objects

flying_test(blu)
flying_test(peggy)

