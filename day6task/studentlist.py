
#LIST OF OBJECTS CONCEPT 

class Students:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myrollno=rollno
        self.myadminno=adminno

obj=[]
obj.append(Students("Rahul",101,50001))
obj.append(Students("bala",103,50002))
obj.append(Students("arif",104,50003))

print(obj[0].myname)
print(obj[1].myname)
print(obj[1].myrollno)



