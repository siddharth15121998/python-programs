
def Addition(num):
    return a+b
def Subtraction(num):
    return a-b
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
        print(Addition(a))
        break

    if choice==2:
        print("Subtraction selected")
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        print(Subtraction(b))
        break

    if choice==3:
        break
    else:
        print("wrong choice")
