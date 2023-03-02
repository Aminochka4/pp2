import re
a =input()
pattern = r"[\s,.]"
print(re.sub(pattern, ":", a))