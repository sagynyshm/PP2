#ex1
import os
res = []
mypath = r'C:\Users\Asus\Desktop\PP2\lab1'
for filename in os.listdir(mypath):
    full_path = os.path.join(mypath, filename)
    if os.path.isfile(full_path):
        res.append(full_path)
print(res)

result=[]
newpath=r'C:\Users\Asus\Desktop\PP2'
for direct in os.listdir(newpath):
    fpath=os.path.join(newpath, direct)
    if os.path.isdir(fpath):
        result.append(fpath)
print(result)

newresult=res+result
print(newresult)

#ex2
import os
def check(path):
    if not os.path.exists(path):
        print(f"\nThe {path} does not exists")
    else:
        print(f"\nThe {path} exist")


    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

path_to_check=r'C:\Users\Asus\Desktop\PP2'
check(path_to_check)

#ex3
import os
path2=r'C:\Users\Asus\Pictures\photo'
if os.path.exists(path2):
    print("The path exists")
    directory = os.path.dirname(path2)
    filename=os.path.basename(path2)
    print("Filename:", filename, "\nDirectory:" , directory)

else:
    print("Path does not exist")


#ex4
def countingLines():
    path4 = r"C:\Users\Asus\Desktop\pp2\lab6\text.txt"
    f = open(path4, "r")
    count = 0
    for i in f:
        if(i != "\n"):
            count += 1
    print("The amount of lines in this file is:", count)
countingLines()
#"C:\Users\Asus\Desktop\pp2\lab6\text.txt"

#ex5

def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')


my_list = [1, 2, 3, 4, 5]
file_name = 'output.txt'
write_list_to_file(my_list, file_name)
print(f"List has been written to {file_name}.")


#ex6
import os

def generate_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(65, 91):  # ASCII values for A-Z
        file_name = os.path.join(directory, chr(i) + ".txt")
        with open(file_name, "w") as file:
            file.write("This is file " + chr(i) + ".txt")

# Directory to store the files
directory = r"C:\Users\Asus\Desktop\pp2\lab6"

# Generate the files
generate_files(directory)

#ex7
def copyPaste():
    patht = r"C:\Users\Asus\Desktop\pp2\lab6\copyfromthis.txt"
    pathOfSecondfile = r"C:\Users\Asus\Desktop\pp2\lab6\copytothis.txt"
    # copying text.txt to text1.txt
    f = open(patht, "r")
    f1 = open(pathOfSecondfile, "w")
    for i in f:
        f1.write(str(i))
    f1.close()
    f.close()

    f1 = open(pathOfSecondfile, "r")
    for i in f1:
        print(i)
copyPaste()

#ex8
def delitingFileInSpecificPath():
    path = r"C:\Users\Asus\Desktop\pp2\lab6\text2.txt"
    if(os.access(path, os.F_OK)):
        print("Your path exist!\nOkay...let me delete your file")
        os.remove(path)
        print("Deleting is succesful! :D")
    else:
        print("Your path does not exist :(")
delitingFileInSpecificPath()