import re
first_name=input("Enter your first name: ")
last_name=input("enter your last name: ")
mobile_num=input("Enter your mobile number: ")
address=input("Enter your address: ")
pincode=input("Enter your pincode: ")
email_id=input("Enter your emailid: ")

def isvalidfirst(first_name):
    valfirst=re.match(r'^(Mr\.|Mrs\.|Ms\.|mr\.|mrs\.|ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$',first_name)
    
    if (valfirst):
        return True
    else:
        return False

def isvalidlast(last_name):
    vallast=re.match(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',last_name)
    if (vallast):
        return True
    else:
        return False

def isvalid(mobile_num):
    r=re.match("(0|91)?[-\s]?[6-9]\d{9}",mobile_num)
    if (r):
        return True
    else:
        return False

    
 
def validateemail(email_id):
    r1= re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$",email_id)
    if (r1):
        return True
    else:
        return False


def validatepincode(pincode):
    r2=re.match("^[5-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
    if (r2):
        return True
    else:
        return False

a=isvalid(mobile_num)
b=validateemail(email_id)
c=validatepincode(pincode)
d=isvalidfirst(first_name)
e=isvalidlast(last_name)


if a and b and c and d and e ==True:
    print("All in correct format")
    print(first_name,last_name)
    print(mobile_num)
    print(address)
    print(pincode)
    print(email_id)
else:
    if a != True:
        print("Enter phone number in CORRECT format")
    if b != True:
        print("enter email in CORRECT format")
    if c != True:
        print("enter pincode in CORRECT format")
    if d != True:
        print("enter first name in CORRECT format")

    if e != True:
        print("enter last name in CORRECT format")



