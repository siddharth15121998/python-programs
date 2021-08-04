import csv
headercontent=["name","rollnum"]
studentdata=[{"name":"anoop","rollnum":23},{"name":"anoopchacha","rollnum":20},{"name":"anoo","rollnum":21},]
with open ("stu.csv","w+",encoding="UTF8",newline="") as s:
    writer=csv.DictWriter(s,fieldnames=headercontent)
    writer.writeheader()
    writer.writerows(studentdata)