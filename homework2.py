import os

def getINodeType(file_name):
    pass

def listEntries(dict):
    pass

def createFiles(dir_name, file_amount):
    pass

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

main()
