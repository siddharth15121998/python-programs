from functools import reduce
l1=[3,2,6,8,4,6,2,9]
sum=reduce(lambda a,b:a+b,l1)
print(sum)