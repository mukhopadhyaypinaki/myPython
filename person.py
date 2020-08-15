class person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is " + str(self.age), "years old")


pinaki = person("Pinaki", 32)

print(pinaki.display())

print(person.getPopulation())

print(person.isAdult(21))

print(pinaki.isAdult(21))
