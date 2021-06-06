# inherits, extend, override
class Employee:

	def __init__(self, name, age,salary):
		self.name = name 
		self.age = age
		self.salary = salary

	def work(self):
		print(f"{self.name} is working...")


class SoftwareEngineer(Employee):

	def __init__(self,name,age,salary, level):
		super().__init__(name,age,salary)
		self.level = level

	def work(self):
		print(f"{self.name} is coding...")



	def debug(self):
		print(f"{self.name} is debugging...")


class Designer(Employee):

	def work(self):
		print(f"{self.name} is designing...")



	def draw(self):
		print(f"{self.name} is drawing...")

se = SoftwareEngineer("Max",26, 6000, "Junior")
se.work()
print(se.name, se.age, se.level)
print(se.debug())

d =  Designer("Philip", 27, 7000)
print(d.name,d.age)
d.draw()
d.work()


# Polymorphism

employee = [SoftwareEngineer("Max",26, 6000, "Junior"),
			SoftwareEngineer("Lisa",26, 6000, "Senior"),
			Designer("Philip", 27, 7000)]



def motivate_employee(employee):
	for employee in employee:
		employee.work()


motivate_employee(employee)

# Recap
# Inheritence: ChildClass(BaseClass)
# Inherit, entend, override
# super().__init__()
# Polymorphism
