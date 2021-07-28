# li=[i for i in range(2,500)]
# li1=[i for i in li if i%2!=0]
# print(li1)
li=["english","tamil","civic,","rotor","example","madam"]
new=[i.replace("madam", "morning") for i in li] 
print(new)