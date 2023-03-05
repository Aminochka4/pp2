path = r"C:\pp2\all labs\lab 6\Directories and files\text.txt"
count = 0
file = open(path, 'r')
#with open(path, 'r) as file:   
for i in file:
    count += 1

print(count)