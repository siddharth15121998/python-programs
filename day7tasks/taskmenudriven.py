class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b
    
class SubtractioOperation:
    def subTwoNum(self,a,b):
        return a-b


class Calculator(AdditionOperation,SubtractioOperation):
    pass

objcalc=Calculator()

while(True):
    print("Select an option from menu ")
    print("\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. exit")
    choice=int(input("enter your choice:"))
    


    if choice==1:
        print("Addition selected")
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        print(objcalc.addTwoNum(a,b))
        

    if choice==2:
        print("Subtraction selected")
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        print(objcalc.subTwoNum(a,b))
        

    if choice==3:
        break
    else:
        print("wrong choice")
