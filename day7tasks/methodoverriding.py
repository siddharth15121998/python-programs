class Car:
    def color(self):
        print("Red")

class BMW(Car):
    def color(self):
        print("White")

obbmw=BMW()
obbmw.color()

obcar=Car()
obcar.color()