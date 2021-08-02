l=[234,567,321,456,874]
try:
    print(l[3])
    #print(a[2])
except (IndexError,NameError):
    print("please enter correct index")

else:
    print("execution completed successfully")
finally:
    print("ok done for the day")

    
    
