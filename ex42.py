## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## creating class Dog which is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## setting passed name value to object name
        self.name = name

## creating class Cat which is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## setting passed name value to object name
        self.name = name

## creating class Person which is-a object
class Person(object):

    def __init__(self, name):
        ## setting passed name value to object name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## creating class Employee which is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## passing the name value to Person __init__()
        super(Employee, self).__init__(name)
        ## setting passed salary to object salary
        self.salary = salary

## creating class Fish
class Fish(object):
    pass

## creating class Salmon which is-a Fish
class Salmon(Fish):
    pass

## creating class Halibut which is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## setting attribute pet of object mary
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()