import re
a = input()
print(re.findall("[A-Z]{1}[a-z]+", a))