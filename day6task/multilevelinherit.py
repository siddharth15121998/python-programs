class India:
    def alotNumber(self,number):

        print(number)
    
class CarManufacturer(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)

class Seller(CarManufacturer):
    def CustomerOrder(self,name,mobno):
        print(name,mobno)

objSeller=Seller()
objSeller.CustomerOrder("Rakesh",9425171349)
objSeller.makeACar("Ford","White",100000)
objSeller.alotNumber("MP15CB0449")
