class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b
    
class SubtractioOperation:
    def subTwoNum(self,a,b):
        return a-b

class MultiplicationOperation:
    def MultiTwoNum(self,a,b):
        return a*b

class Calculator(AdditionOperation,SubtractioOperation,MultiplicationOperation):
    pass

objcalc=Calculator()
n1=int(input("enter a number:"))
n2=int(input("enter second number:"))
print(objcalc.MultiTwoNum(n1,n2))
print(objcalc.addTwoNum(n1,n2))
print(objcalc.subTwoNum(n1,n2))
