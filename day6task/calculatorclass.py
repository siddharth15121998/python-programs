class Calculator:
    def add1(self,a,b):
        return a+b
    
    def mul1(self,a,b):
        return a*b

    def sub1(self,a,b):
        return a-b
    
    def div1(self,a,b):
        return a/b
    
    def floordiv1(self,a,b):
        return a//b

n1=int(input("enter a number:"))
n2=int(input("Enter a number:"))
calc=Calculator()
addme=calc.add1(n1,n2)    
mulme=calc.mul1(n1,n2)    
subme=calc.sub1(n1,n2)    
divme=calc.div1(n1,n2)    
floordivme=calc.floordiv1(n1,n2)
# print(addme)    
# print(subme)    
# print(mulme)    
# print(divme)    
# print(floordivme) 
print(addme,subme,mulme,divme,floordivme)   