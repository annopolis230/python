import csv

with open('employee-logins.csv','r') as file:
    csvfile = csv.reader(file)
    data = [] # Creates a 'holder' for the lists returned by csv.reader to be accessed and filled later on.
    IDs = [] # An empty list to store UserIDs. Later this will be used to assist in detecting duplicates in the data.
    outputList = [] # An empty list that will eventually be used to hold the modified data and be written to a file and printed to the console.

    for line in csvfile:
        data.append(line) # Fills the data list.
        IDs.append(line[0]) # Fills the IDs list.

    def findDuplicates(array): # This function returns a list containing the UserIDs of duplicate entries.
        return list(set([x for x in array if array.count(x) > 1])) # Uses list comprehension to create a new list containing all UserIDs that have duplicates. This will return ['3','18','7','8'].

    def calculateDuplicateLogins(duplicateIDs): # This function will do two things: 1) Condense duplicate entries into a single list and calculate total login attempts.
         #2) Append a single list per duplicate UserID that contains the UserID, first name, last name, and sum of login attempts to the data list.
        result = []
        for i in range(len(duplicateIDs)): # duplicateIDs is the list returned by calling findDuplicates(IDs). It has a length of 4 in this instance. 
            temp = [] # Clears the temp list or creates a new one
            for line in data:
                if line[0] == duplicateIDs[i]: # Checking if the current iteration of the data list lines up with a UserID in the duplicateIDs list.
                    if line[1] and line[2] not in temp: # This prevents UserID, firstName, and lastName from being appended multiple times to the same list.
                        temp.append(line[0]) # Adds UserID to the temp list.
                        temp.append(line[1]) # Adds firstName to the temp list.
                        temp.append(line[2]) # Adds lastName to the temp list.
                    temp.append(int(line[4])) # Adds # of login attempts to the temp list. 
            result.append(temp) # Creates a 2 dimensional array with the data from the temp lists as elements
        for n in result:
            logins = sum(n[3:5]) # Adds the last two values of the list. These values are the # of login attempts by each duplicate. 
            del n[-2:] # Deletes the values the last statement just used to get the sum. 
            n.insert(3,logins) # Inserts the new calculated sum into the list.
        for x in result: # This loops over the modified data in the result list and adds each element to the data list. 
            data.append(x) 
    
    calculateDuplicateLogins(findDuplicates(IDs))
    data.pop(0)
    for i in range(3): # This purpose of this block is to remove all instances of duplicate UserIDs in the data list. These need to be removed because the previous function just parsed the duplicates, so they are no longer necessary. 
        for line in data:
            if (line[0] in findDuplicates(IDs)) and len(line) == 6: # Checking if the line is a duplicate and if it hasn't been added by the previous function. The previous function adds a list of length 4. 
                data.remove(line)
            if len(line) == 6: # This removes unnecessary information from the lines, including IP address and login period. 
                del line[3:7:2]
            
    for i in data:
        if int(i[3]) >= 250: # Checks for suspicious users categorized by 250 or greater login attemps.
            outputList.append(i) # If the user is suspicious, their data is appended to the outputList. 

    newFile = open("suspiciousLogins.txt","w")
    newFile.write("\nSuspicious login attempts: ")
    newFile.write("\nID, FirstName, LastName, # of login attempts")
    for i in outputList: # This loop will add the information of suspicious users to the text file created by a previous line.
        listString = ' '.join(map(str,i)) # This uses the map() method to convert the suspicious user's information list into a string, making it easier to write to a text file. 
        newFile.write('\n'+listString)
    newFile.close()
    print("Suspicious login attempts of the employee-logins.csv file: ")
    print("ID,    FirstName,  LastName, # of login attempts")
    for i in outputList: # Prints suspicious login information to the console. 
        print(i)
