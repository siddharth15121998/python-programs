import json
import  requests
d=requests.get("https://reqres.in/api/users?page=2")
ED=d.json()  
#print(ED)
data=ED['data']
print(data)
for i in data:
    first_name=i['first_name']
    print(first_name)
