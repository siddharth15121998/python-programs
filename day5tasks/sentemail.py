import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("hariompateldada@gmail.com","Sparsh@01")
message="hello all, I hope you all are doing great.hello all, I hope you all are doing great."
connection.sendmail("hariompateldada@gmail.com",["chedivya1998@gmail.com","	ridhimathur10@gmail.com"],message)
print("Email has sent succesfully")
connection.quit()
