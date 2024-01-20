path = './data/notes.txt'
idPath = './data/id.txt'

# write the content of the task to the save file
def writeNotes(content):
    lineId = parseLength() + 1
    with open(path, 'a', encoding='utf-8') as FILE:
        FILE.write(f"{lineId}: {content}")

    with open(idPath, 'a', encoding='utf-8') as IDFILE:
        IDFILE.write(lineId)
        


# read content of the save file and return it in a list
def readNotes():
    returnList = []
    with open('./data/notes.txt', 'r', encoding='utf-8') as FILE:
        for line in FILE:
            line = line.rstrip()

            # Check if the line is whitespace
            if not line:
                returnList
            # if not whitespace put value of line in the list to return
            else:
                returnList += [line]

        # if the file is empty return None
        if not returnList:
            return None
    return returnList



# completely empty the save file
def clearNotes():
    with open(path, 'w', encoding='utf-8') as FILE:
        FILE.truncate(0)

    with open(idPath, 'w', encoding='utf-8') as IDFILE:
        IDFILE.truncate(0)



# return the length of a given file.    
def parseLength():
    count = 0
    with open('./data/notes.txt', 'r', encoding='utf-8') as FILE:
        for line in FILE:
            line = line.rstrip()

            # Check if the line is whitespace
            if not line:
                count
            else:
                count+=1
    return count