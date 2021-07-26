class Cars:
    def mineColor(self,color):
        self.color=color
        print(self.color)

class BMW(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)

objcars=Cars()
objBMW=BMW()
# objcars.mineColor("Red")
# objcars.topSpeed(100)         #error
objBMW.mineColor("white")
objBMW.topSpeed(150)