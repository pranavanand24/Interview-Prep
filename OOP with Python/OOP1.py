# class
class SoftwareEngineer:

	#class attribute
	alias = "Keyboard Magician"

	def __init__(self,name,age,level,salary):
		#instance attributes
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary



# instance 
se1 = SoftwareEngineer("Max",20,"Junior",5000)
print(se1.name,se1.age)
print(SoftwareEngineer.alias)

se2 = SoftwareEngineer("Lisa",25,"Senior",7000)
print(se2.level,se2.salary)


# Summary


# create a class(blueprint)
# create a instance(object)
# class vs instance
# instance attribute: defined in __init__(self)
# class attribute