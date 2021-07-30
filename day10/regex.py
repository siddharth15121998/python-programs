import re
#   "^hello"     matches any string that start with hello
#   "hello$"     matches any string that end with hello
#   "^hello$"    matches any string that starts and end with hello
#   "hello"      matches any string that contains hello
#   "hello*"     matches any string that contains 0 or more than O's
#   "hello+"     matches any string that contains 1 or more than O's
#   "hello?"     there might be a single O(letter o) or not.
#   {}           to specify range
#   ()           for group
#   |(or)
var="a56%"
#regex=re.match("^(bc){2,4}$",var)
#re1=re.match("(hello|hii)+x",var)
re2=re.match("^(\+91)?[0]?(91)?[6-9]\d{9}$",var)
#v=re.search("hello+",var)
#v2=re.search("hello*",var)
#v1=re.search("hello?",var)
print(re2)
