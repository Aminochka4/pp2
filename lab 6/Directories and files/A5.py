path  = r"C:\pp2\all labs\lab 6\Directories and files\text.txt"
file = open(path, 'a')
a = ["\n", "my", "favorite", "song"]
for i in a:
    file.write(i + " ")
file.close()

file = open(path, 'r')
print(file.read())
