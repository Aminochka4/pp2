import os
path = r"C:\pp1"

#1
if os.access(path, os.F_OK):
    print (f"{path} exists")
else:
    print (f"{path} does not exist")

#2
if os.access(path, os.R_OK):
    print (f"{path} is readable")
else:
    print (f"{path} is not readable")

#3
if os.access(path, os.W_OK):
    print (f"{path} is writable")
else:
    print (f"{path} is not writable")

#4
if os.access(path, os.X_OK):
    print (f"{path} is executable")
else:
    print (f"{path} is not executable")

