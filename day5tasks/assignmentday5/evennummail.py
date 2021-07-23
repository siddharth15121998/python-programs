import smtplib
li=[]
evenmsg=[]
for i in range(10):
    n=int(input("Enter the number :"))
    li.append(n)
for num in li:
    if(num%2==0):
        evenmsg.append(num)

msg=' '.join(map(str,evenmsg))
#

# print(msg)
    
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("hariompateldada","Sparsh@01")
#msg="Hello there , good evening"
connection.sendmail(,"hariompateldada@gmail.com","ridhimathur10@gmail.com",msg)
print("email has successfully send")
connection.quit()