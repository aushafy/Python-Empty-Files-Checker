import os as os # import os module

print("Enter your absolute directory to scanning empty files")
print("Example: D:/BecomePythonDev/example/")

path = input(": ")

x = []

for file_obj in os.scandir(path):
    if file_obj.is_file():
        f = file_obj.name
        x.append(f) # name of each file in the directory are stored in list of x

for files in x:
    with open(path + files) as file_obj:
        lines = file_obj.readlines()
        file_len = len(lines)
        if file_len == 0:
            print("{0} is empty file!".format(files))
        else:
            print("{0} has {1} lines!".format(files, file_len))