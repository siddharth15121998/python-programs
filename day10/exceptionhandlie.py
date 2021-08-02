try:
    n1=int(input("Enter a number:"))
    n2=int(input("Enter second number:"))
    div=n1/n2               #CAN CREATE EXCEPTION
    print(div)

except ZeroDivisionError:
    print("OOPS!, division by zero is not allowed")
except ValueError:
    print("Only number should be entered")

    