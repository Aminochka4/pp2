import re
a = input()
pattern = r"([A-Z])"
print(re.sub(pattern, r" \1", a))