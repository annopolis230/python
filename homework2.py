import os

def getINodeType(file_name):
    return os.stat(os.path.join(os.getcwd(),file_name)).st_ino

def listEntries(dict):
    pass

def createFiles(dir_name, file_amount):
    os.chdir(dir_name)
    fileNum = 0
    for i in range(file_amount):
        fileNum+=1
        fileName = "file_"+str(fileNum)+".xls"
        open(fileName,"a")

def createSubDirectories(dir_name, subdir_amount):
    pass

def renameFiles(dir_name, current_ext, new_ext):
    pass

def main():
    currentDirectory = os.getcwd()
    print(currentDirectory)
    os.makedirs(os.path.join(currentDirectory, "Lab3"))
    os.chdir("Lab3")
    print(os.getcwd())
    createFiles(os.getcwd(),5)
    
    
main()
