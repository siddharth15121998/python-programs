# import logging
# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
# logging.basicConfig(filename="demo.log",level=logging.DEBUG)
# try:
#     z=n1/n2
#     print(z)
# except:
#     logging.info("something went wrong")
import glob
for i in glob.glob('day12/col*.py'):
    print(i)