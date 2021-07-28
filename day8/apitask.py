import json
import  requests
data=requests.get("https://jsonplaceholder.typicode.com/posts") 
ExtractedData=data.json()      #json parsing #print(ExtractedData) 
li=[]
for i in ExtractedData:
    li.append(i["title"])
lis=[x for x in li if x[0]=="a"in x]
lis.append(li)
print(lis)
    





   

