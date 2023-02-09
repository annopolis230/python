import os, stat

currentDirectory = os.getcwd()

def getINodeType(file_name):
    return os.stat(os.path.join(os.getcwd(),file_name)).st_ino

def listEntries(dict):
    print("File name    File type")
    for i in dict.items():
        print(i)

def createFiles(dir_name, file_amount):
    os.chdir(dir_name)
    fileNum = 0
    for i in range(file_amount):
        fileNum+=1
        fileName = "file_"+str(fileNum)+".xls"
        open(fileName,"a")
    for file in os.listdir(os.getcwd()):
        os.chmod(file,stat.S_IRWXU | stat.S_IRGRP)

def createSubDirectories(dir_name, subdir_amount):
    os.chdir(dir_name)
    dirNum = 0
    for i in range(subdir_amount):
        dirNum+=1
        dirName = "dir_"+str(dirNum)
        os.makedirs(os.path.join(os.getcwd(), dirName))
        
def renameFiles(dir_name, current_ext, new_ext):
    os.chdir(dir_name)
    index = 0
    for file in os.listdir(os.getcwd()):
        index += 1
        fileName = "file_"+str(index)+str(current_ext)
        newName = "file_"+str(index)+str(new_ext)
        if not (os.path.exists(fileName)):
            break
        else:
            os.rename(fileName,newName)
        
def main():
    lab3Dict = {}
    print(currentDirectory)
    os.makedirs(os.path.join(currentDirectory, "Lab3"))
    os.chdir("Lab3")
    print(os.getcwd())
    while True:
        filesToCreate = int(input("Enter how many files to create: "))
        if filesToCreate < 0:
            print("Input must be above 0")
        else:
            break
    createFiles(os.getcwd(),filesToCreate)
    while True:
        dirsToCreate = int(input("Enter how many subdirectories to create: "))
        if dirsToCreate < 0:
            print("Input must be above 0")
        else:
            break
    createSubDirectories(os.getcwd(),dirsToCreate)
    renameFiles(os.getcwd(),".xls",".docx")
    for file in os.listdir(os.getcwd()):
        lab3Dict.update({file:getINodeType(file)})
    listEntries(lab3Dict)
    
main()

