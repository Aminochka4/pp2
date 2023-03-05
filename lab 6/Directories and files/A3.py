import os

path = r"C:\pp1"

if os.access(path, os.F_OK):
    print (f"the path {path} includes:")
    for i in os.listdir(path):
        print(i)
else:
    print (f"{path} does not exist")