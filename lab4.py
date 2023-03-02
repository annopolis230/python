from zipfile import ZipFile
import shutil
import os
import time
import inspect

def doesExist(dir, ident): # This function is used in a lot of places in order to not reuse code. It checks if a specified path exists.
    if not os.path.exists(dir):
        print(ident,"unknown, try again") # If the path doesn't exist, it will print what doesn't exist. This information is supplied by the caller. 
        return False
    return True

def backup(source,destination):
    while True:
        if doesExist(source, "backup source") and doesExist(destination, "backup destination"): # Checking the source and destination directories exist
            files = os.listdir(source)
            for file in files:
                shutil.copy2(os.path.join(source,file),destination) # Uses the copy2 method from shutil to copy the files from the source and paste them into the destination.
            print("Backup successful")
            break
        elif not os.path.exists(source):
            source = input("Enter another source for the backup function: ")
        elif not os.path.exists(destination):
            destination = input("Enter another destination for the backup function: ")
            
def archive(dir):
    while True:
        if doesExist(dir, "archive source"): # Checking if the directory to be archived exists or not
            validArchives = ['zip','gztar','tar','bztar','xztar']
            print("Valid archive types are: ")
            for i in validArchives:
                print(i)
            while True:
                archiveType = str(input("Enter the type of archive to create: "))
                if archiveType not in validArchives: # Checks if the archive type given by the user is a valid type
                    print("Invalid archive type.")
                else:
                    break
            shutil.make_archive("archive",archiveType,dir) # Uses the make_archive method from shutil to create the appropriate archive. 
            print(archiveType,"archive successful as archive."+str(archiveType))
            break
        else:
            dir = input("The source directory could not be found. Try again: ")

def getSize(zipFile):
    while True:
        if not doesExist(zipFile, "zipfile"):
            zipFile = input("Enter a valid zip file name: ")
        else:
            break
    size = int(input("Enter size threshold: "))
    print("Displaying files inside",zipFile,"with size greater than",size)
    with ZipFile(zipFile, 'r') as file:
        for i in file.namelist():
            info = file.getinfo(i)
            if info.file_size >= size:
                print(i,info.file_size)

def displayModifiedFiles(dir):
    directory = dir
    if not doesExist(dir, "modified source"): # If the directory supplied doesn't exist, the function will use the current directory instead.
        directory = os.getcwd()
    os.chdir(directory)
    print("Displaying items modified within the last 30 days in",directory)
    for file in os.listdir(os.getcwd()): # Looping through all items in the given directory
        if (int(time.time()) - int(os.path.getmtime(file))) <= 2592000: # This checks if an item was modified in the last 30 days by subtracting the current
             # unix time from the last modified unix time of the item. If it's less than 2592000 seconds (30 days), the file will be printed.
            print(file)

def main():
    functionDict = {
        'backup':backup,
        'archive':archive,
        'getsize':getSize,
        'displaymodifiedfiles':displayModifiedFiles
    } # This is a dictionary that stores the functions to be called by a user in the program. 

    while True: # The program is in a loop so the user can decide when to exit.
        print("The valid functions are: ")
        for function in functionDict.keys():
            print(function)
        while True: # This loop just checks the given function name exists.
            toRun = input("Enter the name of the function to execute: ")
            if toRun.lower() not in functionDict:
                print("Invalid function name.")
            else:
                break
        print(toRun,"takes these arguments:\n",inspect.signature(functionDict[toRun.lower()])) # Uses inspect.signature to print the required arguments for the given function.
        promptString = "Enter first argument for "+str(toRun)+": "
        arg1 = str(input(promptString))
        try: # This try block will catch any exception caused by supplying a function with not enough arguments. 
            functionDict[toRun.lower()](arg1)
        except TypeError: # If more arguments are required, the user is prompted to enter another. 
            promptString = "Enter second argument for "+str(toRun)+": "
            arg2 = str(input(promptString))
            functionDict[toRun.lower()](arg1,arg2) # Calls the given function with both required arguments. 
        continueProgram = str(input("Would you like to continue the program? Type Y or N. "))
        if continueProgram.upper() == "N":
            break
main()
