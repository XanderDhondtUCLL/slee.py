path = r'.\data\notes.txt'

# write the content of the task to the save file
def writeNotes(content):
    lineId = parseLength() + 1
    with open(path, 'a', encoding='utf-8') as FILE:
        FILE.write(f"{lineId}. {content}\n")



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
    count = 0

    # read the content of the file first before wiping it
    noteContents = readNotes()

    # wipe the file and do not add corresponding id's
    with open(path, 'w', encoding='utf-8') as FILE:
        print(noteContents)
        for line in noteContents:
            # if the start id of the line matches the id, write it to the new file and change its number
            if line[0] != id:
                count += 1
                FILE.write(f"{count}{line[1::]}\n")

# completely empty the save file
def clearNotes():
    with open(path, 'w', encoding='utf-8') as FILE:
        FILE.truncate(0)


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