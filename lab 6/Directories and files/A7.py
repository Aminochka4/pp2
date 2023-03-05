path_original = r"C:\pp2\all labs\lab 6\Directories and files\text.txt"
path_copy = r"C:\pp2\all labs\lab 6\Directories and files\copy.txt"
file1 = open(path_original, 'r')
file2 = open(path_copy, 'w')
for i in file1:
    file2.write(i)
file1.close()
file2.close()

file2 = open(path_copy, 'r')
print(file2.read())