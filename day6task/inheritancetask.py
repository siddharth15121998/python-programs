class Animals:
    def iEat(self,eat):
        self.eat=eat
        print(self.eat)
class Dog(Animals):
    def iSound(self,sound):
        self.sound=sound
        print(self.sound)

objAnimals=Animals()
objDog=Dog()

objAnimals.iEat("meat")
objDog.iSound("bark")

