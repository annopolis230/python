import csv

with open('employee-logins.csv','r') as file:
    csvfile = csv.reader(file)
    data = []
    IDs = []

    def findDuplicates(array):
        return list(set([x for x in array if array.count(x) > 1]))

    def calculateDuplicateLogins(duplicateIDs):
        for i in range(len(duplicateIDs)):
            temp = []
            for line in data:
                if line[0] == duplicateIDs[i]:
                    if line[1] and line[2] not in temp:
                        temp.append(line[0])
                        temp.append(line[1])
                        temp.append(line[2])
                    temp.append(int(line[4]))
            data.append(temp)
        
    for line in csvfile:
        data.append(line)
        IDs.append(line[0])

    data.pop(0)
    for line in data:
        if line[0] in findDuplicates(IDs):
            data.remove(line)
    
    for line in data:
        print(line)

    calculateDuplicateLogins(findDuplicates(IDs))
    for line in data:
        print(line)
