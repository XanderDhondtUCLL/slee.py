from tkinter import *
from slee import *

# Setup
background_color = '#191919'
foreground_color = '#F5F5F5'

# Function to update notes in the GUI
def update_notes():
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
    top = Toplevel(window)
    top.geometry("420x200")
    top.title("adding task")
    top.config(background=background_color)

    label = Label(top, 
                  text='Add task:', 
                  font=('Arial 18 bold'),
                  fg=foreground_color,
                  background=background_color)
    label.pack(anchor=NW)

    entry = Entry(top)


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

button = Button(btnFrame, text='Add note', command=addPopup)
button.pack()

# Update notes initially
update_notes()

window.mainloop()