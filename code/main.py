from tkinter import *
from slee import *

# Setup
background_color = '#191919'
foreground_color = '#F5F5F5'

# Function to update notes in the GUI
def update_notes():
    # Clear existing labels
    for item in itemFrame.winfo_children():
        item.destroy()

    # Create and pack new labels
    for note in readNotes():
        label = Label(itemFrame, 
                      text=note,
                      wraplength=300,
                      font='Arial',
                      fg=foreground_color,
                      bg=background_color)
        label.pack(side=TOP, anchor=W)

# Function to open popup window upon pressing add button
def addPopup():
    # Function to add tasks to the file
    def fileWrite():
        value = entry.get()
        writeNotes(value)
        update_notes()

    top = Toplevel(window)
    top.geometry("420x100")
    top.title("adding task")
    top.config(background=background_color)

    label = Label(top, 
                  text='Add task:', 
                  font=('Arial 18 bold'),
                  fg=foreground_color,
                  background=background_color)
    label.pack(anchor=NW)

    entry = Entry(top)
    entry.pack(expand=YES, fill=X, padx=10)
    
    submitBtn = Button(top,
                       text='add task',
                       command=fileWrite)
    submitBtn.pack(pady=5)

# GUI setup
window = Tk()
window.geometry("420x420")
window.title("slee.py")
window.config(background=background_color)

# Main
itemFrame = Frame(window, background=background_color)
itemFrame.pack(side=TOP, fill=BOTH, expand=YES)

btnFrame = Frame(window)
btnFrame.pack(side=BOTTOM, padx=10 ,pady=10)

button = Button(btnFrame, text='Add task', command=addPopup)
button.pack()

# Update notes initially
update_notes()

window.mainloop()