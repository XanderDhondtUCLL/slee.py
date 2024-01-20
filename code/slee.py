path = r'..\data\notes.txt'
idPath = r'..\data\id.txt'

# write the content of the task to the save file
def writeNotes(content):
    lineId = parseLength() + 1
    with open(path, 'a', encoding='utf-8') as FILE:
        FILE.write(f"{lineId}. {content}\n")

    with open(idPath, 'a', encoding='utf-8') as IDFILE:
        IDFILE.write(f'{str(lineId)}\n')



# read content of the save file and return it in a list
def readNotes():
    returnList = []
    with open(path, 'r', encoding='utf-8') as FILE:
        for line in FILE:
            line = line.rstrip()

            # Check if the line is whitespace
            if not line:
                returnList
            # if not whitespace put value of line in the list to return
            else:
                returnList += [line]

    return returnList



# remove a specific task if completed
def removeNote(id):
    parseLength('')




# completely empty the save file
def clearNotes():
    with open(path, 'w', encoding='utf-8') as FILE:
        FILE.truncate(0)

    with open(idPath, 'w', encoding='utf-8') as IDFILE:
        IDFILE.truncate(0)



# return the length of a given file.    
def parseLength():
    count = 0
    with open(path, 'r', encoding='utf-8') as FILE:
        for line in FILE:
            line = line.rstrip()

            # Check if the line is whitespace
            if not line:
                count
            else:
                count+=1
    return count