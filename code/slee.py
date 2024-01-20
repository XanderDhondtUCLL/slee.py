def writeNotes(content):
    with open('.../data/notes.txt', 'a', encoding='utf-8') as FILE:
        FILE.write(content)

def readNotes():
    with open('.../data/notes.txt', 'r', encoding='utf-8') as FILE:
        for line in FILE:
            print(line.rstrip())

def clearNotes():
    with open('.../data/notes.txt', 'w', encoding='utf-8') as FILE:
        FILE.truncate(0)

writeNotes('Nea')