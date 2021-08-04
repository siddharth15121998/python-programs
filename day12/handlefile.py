import logging
import time
myfile=open('namefile.txt','w')

logging.basicConfig(filename="demolog1.log",level=logging.DEBUG)
while (True):
    print("\nfile demonstration menu")
    
    print("1. Add a name")
    print("2. View names")
    print("3. Exit")
    try:
        choice=int(input("Enter  choice "))
        logging.info("User enterd correct choice")
    except:
        logging.error("something went wrong")
        continue

    if choice==1:
        n=input("enter  name :")
        myfile=open("namefile.txt",'a')
        myfile.write(n+" ")
        current_time=time.localtime()
        current_time_format=time.strftime("%H:%M:%S",current_time)
        print("file updated on ",current_time_format)
    if choice==2:
        print("Displaying names in files ")
        myfile=open('namefile.txt','r')
        x =myfile.read()
        print(str(x))
    if choice==3:
        break  
myfile.close