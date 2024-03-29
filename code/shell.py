from slee import *
main = True

while main:

    print("\n-=-=-=- SLEE.PY NOTES -=-=-=-\n")
    for task in readNotes():
        print(task)
    print('')

    print("select one of following operations: (give in one of the numbers)")
    print("1: add todo\n2: remove todo\n3: clear entire list\n4: leave slee.py notes")

    value = input('\n')
    
    match value:
        case '1':
            content = input("\nadding todo: ")
            writeNotes(content)

        case '2':
            removeID = input("\nremove todo (please give ID): ")
            removeNote(removeID)

        case '3':
            print("-=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-")
            clear = input('are you sure you want to do this? y/n: ')

            if clear == 'y':
                clearNotes()
            else:
                print('-=-=-=- -=-=-=- -=-=-=-\n\naborting\n\n-=-=-=- -=-=-=- -=-=-=-')

        case '4':
            print("\n-=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-\n Thank you for using the program\n©Alnea 2024")
            break

        case _:
            print('-=-=-=- -=-=-=- -=-=-=-\n\nwhat the actual fuck?\n\n-=-=-=- -=-=-=- -=-=-=-')