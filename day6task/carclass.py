class Cars:
    color="black"
    brand="BMW"

    def findMileage(self,li,km):
        return km/li


myCar=Cars()
a1=input("enter color:")
a2=input("enter brand:")

l=int(input("enter litres:"))
k=int(input("Enter kilometers:"))
mileage=myCar.findMileage(l,k)

myCar.color=a1
myCar.brand=a2
print(myCar.color)
print(myCar.brand)
print(mileage)

#printing default values using object
# defaultCar=Cars()
# print(defaultCar.color)
# print(defaultCar.brand)
