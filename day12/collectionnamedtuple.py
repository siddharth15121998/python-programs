import collections
employees=collections.namedtuple("employees",["name","empid","salary"])
e1=employees("Raju","101","25000")
print(e1.name)
print(e1[1])