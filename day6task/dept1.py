class Department:
    def __init__(self,dept):
        self.dept=dept
    def addStudents(self):
        self.Sname=input("enter your name :")
        self.Sroll=int(input("enter your roll :"))
        self.Sadmin=int(input("enter your admisno :"))
        self.Scollege=input("enter your college :")
        self.Sadd=input("enter your address :")
        self.Smob=int(input("enter your smob :"))
        print("Department is :", self.dept)
        print("Student name is :", self.Sname)
        print("Student roll number is :", self.Sroll)
        print("Student admission number is :", self.Sadmin)
        print("Student college is :", self.Scollege)
        print("Student mobile is :", self.Smob)
dname=input("Enter department name:")
s1=Department(dname)
s1.addStudents()
print("\n")
s2=Department("ECE")
s2.addStudents()
