class Department:
    def __init__(self,deptn):
        self.deptn=deptn
        
    def addStudents(self,sname,sroll,sadmin,saddr,scollege,smob):
        self.sname=sname  
        self.sroll=sroll
        self.saddr=saddr
        self.scollege=scollege
        self.smob=smob
        self.sadmin=sadmin
           
        print("department:",self.deptn)
        print("name:",self.sname)
        print("rollnumber:",self.sroll)
        print("address:",self.saddr)
        print("college:",self.scollege)
        print("mobile:",self.smob)
        print("admission:",self.sadmin)

s1=Department("CSE")
s1.addStudents("siddharth",1056,"sagar","BTIRT",9425171349,501)


        
    



