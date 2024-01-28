from tkinter import *
from slee import *

# button functions
def update():
    for item in itemFrame.winfo_children():
        item.destroy()
    
    for item in readNotes():
        label = Label(itemFrame, text=item, font='Arial 16 bold',fg=foreground_color, bg=background_color,wraplength=380)
        label.pack(anchor='w')

# window + functionality to add tasks
def addPopup():
    def writeTask():
        value = entry.get()
        writeNotes(value)
        update()
    
    popup = Toplevel(bg=background_color)
    popup.geometry('300x100')
    popup.title('Remove Task')

    Label(popup, text='Add task:', font='Arial 12 bold',fg=foreground_color,bg=background_color).pack(anchor='nw', padx=10, pady=5)
    entry = Entry(popup)
    entry.pack(fill=X, padx=10)
    Button(popup, text='add', command=writeTask).pack(side=LEFT, padx=10)

# window + functionality to remove tasks
def removePopup():
    def updateTasks():
        tasks = []
        for item in readNotes():
            tasks += [item]
        return tasks

    def removeTask():
        selectedId = selectedValue.get()[0]
        removeNote(selectedId)
        update()

    popup = Toplevel(bg=background_color)
    popup.geometry('300x120')
    popup.title('Remove Task')

    Label(popup, text='Remove task:', font='Arial 12 bold', fg=foreground_color, bg=background_color).pack(anchor='nw', padx=10, pady=5)

    # dropdown functionality
    tasks = updateTasks()
    selectedValue = StringVar()
    dropDown = OptionMenu(popup, selectedValue, *tasks)
    dropDown.config(width=20)
    selectedValue.set(tasks[0])
    dropDown.pack(anchor='w', padx=10)

    Button(popup, text='remove', command=removeTask).pack(side=LEFT, padx=10)


# Setup
background_color = '#191919'
foreground_color = '#F5F5F5'

window = Tk()
window.geometry('420x500')
window.maxsize(width=420, height=500)

# create a container frame
containerFrame = Frame(window, bg=background_color)
containerFrame.pack(fill=BOTH, expand=True)

# create main frame
mainFrame = Frame(containerFrame)
mainFrame.pack(side=TOP, fill=BOTH, expand=True)

# create the canvas
canvas = Canvas(mainFrame, bg=background_color, borderwidth=0, highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# create the scrollbar
itemScrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
itemScrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
canvas.configure(yscrollcommand=itemScrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1 * (event.delta/120)), "units"))

# add itemFrame to window in the canvas
itemFrame = Frame(canvas, bg= background_color)
canvas.create_window((0,0), window=itemFrame, anchor='nw')

# create button frame
buttonFrame = Frame(containerFrame, bg=background_color)
buttonFrame.pack(side=BOTTOM)

# create buttons in the button frame
Button(buttonFrame, text="add task", command=addPopup).pack(side=LEFT, padx=5, pady=10)
Button(buttonFrame, text="remove task", command=removePopup).pack(side=LEFT, padx=5, pady=10)

# call update once upon loading of program
update()
window.mainloop()
