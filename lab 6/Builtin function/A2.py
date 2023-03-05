a = input()
cntup = 0
cntlow = 0
for i in a:
    cntup += int(i.isupper())
    cntlow += int(i.islower())
print (cntup, cntlow)