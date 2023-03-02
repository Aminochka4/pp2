import re
def f(Object):
    return Object.group("t1")+ "_" + Object.group("t2").lower()

a = input()
pattern = "(?P<t1>[a-z])(?P<t2>[A-Z])+"
print (re.sub(pattern, f, a))