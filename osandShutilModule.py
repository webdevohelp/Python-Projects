import os
f = open('practice.txt','w+')
#to create a file
f.write('this is text')
#to write something to the file
f.close()
#to close the file

print(os.getcwd())
#to see CWD
print("\n")
print(os.listdir(os.getcwd()))
#to see all contects of Current Working Directory

file = open("hello.txt","w+")
file.write("Hello dude!")
file.close()
try:
    os.unlink("hello.txt")
    #this deletes the file named hello.txt and Note that OS Module permanently deletes all files so use it very carefully
    print("\nDeleted the file like a hero!!!")
    print()
except:
    print("Cant delete hello.txt")


import shutil
try:
    shutil.move('d:\\practice\\practice.txt','d:\\practice\\Python Practice',)
    #to move file from one folder to another
except:
    print("\nFile already exists at destination!")


#pip install send2trash
import send2trash
try:
    send2trash.send2trash("practice.txt")
    print("\nFile practice.txt Moved to Trashbin of send2trash module!")
except:
    print("Already moved to trash!")


#os.walk module
print(os.walk("D:\\Practice\\Python Practice"))
for folder, sub_folders, files in os.walk("D:\\Practice\\Python Practice"):
    print(f"Currently looking at {folder}\n")
    print(f"Subfolders are : ")
    for sub_fold in sub_folders:
        print(f"\tSub-Fulder: {sub_fold}")
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"\tFiles: {f}")
    print("\n")