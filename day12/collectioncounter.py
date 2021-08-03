import collections

# x=collections.Counter(["Hello","Hii","Hello"])
# print(x)
l=[]
for i range(1,11):
    name=input("Enter names")
    l.append(name)
count=collections.Counter(l)
print(count)





