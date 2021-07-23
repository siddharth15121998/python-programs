n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
large=[]
small=[]
def compareMe(n1,n2):
    if n1>n2:
        large.append(n1)
        small.append(n2)
    else:
        small.append(n1)
        large.append(n2)

compareMe(n1,n2)
print(large)
print(small)