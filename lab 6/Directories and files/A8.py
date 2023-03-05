import os
os.chdir(r"C:\pp1")

open("example.txt", 'a').close()

print(os.listdir())

if os.path.exists("example.txt"):
    os.remove("example.txt")

print(os.listdir())