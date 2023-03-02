import re
a = input()
pattern = "[A-Z]+"
print(re.sub(pattern, " ", a))