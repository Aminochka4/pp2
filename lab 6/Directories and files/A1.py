import os
path = r"C:\pp1"
directories_files = os.listdir(path)

#1 only directories
for i in directories_files:
    if os.path.isdir(os.path.join(path, i)):
        print(i)

print()

#2 files and directories
for i in directories_files:
    print(i)

print()

#3 only files
for i in directories_files:
    if os.path.isfile(os.path.join(path, i)):
        print(i)
    

