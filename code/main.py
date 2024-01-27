from tkinter import *
from slee import *


def update():
    for item in itemFrame.winfo_children():
        item.destroy
    
    for item in readNotes():
        label = Label(itemFrame, text=item)
        label.bind('<Configure>', lambda e: label.configure(wraplength=label.winfo_width()))
        label.pack(side=LEFT)

# Setup
background_color = '#191919'
foreground_color = '#F5F5F5'

window = Tk()
window.geometry('420x500')
window.maxsize(width=420, height=500)

# create a container frame
containerFrame = Frame(window)
containerFrame.pack(fill=BOTH, expand=True)

# create main frame
mainFrame = Frame(containerFrame)
mainFrame.pack(side=TOP, fill=BOTH, expand=True)

# create the canvas
canvas = Canvas(mainFrame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# create the scrollbar
itemScrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
itemScrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
canvas.configure(yscrollcommand=itemScrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1 * (event.delta/120)), "units"))

# add itemFrame to window in the canvas
itemFrame = Frame(canvas)
canvas.create_window((0,0), window=itemFrame, anchor='nw')

# create button frame
buttonFrame = Frame(containerFrame)
buttonFrame.pack(side=BOTTOM)

# create buttons in the button frame
Button(buttonFrame, text="Button 1").pack(side=LEFT, padx=5, pady=10)
Button(buttonFrame, text="Button 2").pack(side=LEFT, padx=5, pady=10)

# call update once upon loading of program
update()
window.mainloop()
