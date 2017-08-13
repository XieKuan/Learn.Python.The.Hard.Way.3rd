## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def _init_(self, name):
		## ??
		self.name = name

## Cat is-a Animal too
class Cat(Animal):

	def _init_(self, name):
		## ??
		self.name = name

## Person is-a object
class Person(object):

	def _init_(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def _init_(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self)._init_(name)
		## ??
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog named "Rover"
rover = Dog("Rover")

## satan is-a Cat named "Satan"
satan = Cat("Satan")

## mary is-a Person named "Mary"
mary = Person("Mary")

## mary has-a pet named rover
mary.pet = rover

## frank is-a Employee named "Frank" with 120000 salary
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()