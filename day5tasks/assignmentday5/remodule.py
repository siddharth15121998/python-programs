import re

txt = "The Prime Minister of india"
x = re.findall("in", txt)
print(x)