import re
a = input()
pattern = "a.*b$"
print(re.search(pattern, a))