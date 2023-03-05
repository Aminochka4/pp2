import os
path = r"C:\pp1\examples_for_lab"
name_of_files = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in name_of_files:
    os.chdir(path)#чтобы показать путь для создания файлов
    open(f"{i}.txt", 'a').close() #создает файлы
    #os.replace(open(f"{i}.txt", "w"), path)
