from tkinter import *
from slee import *

# setup #
running = True

window = Tk()
window.geometry("420x420")
window.title("slee.py")
window.config(background="#191919")

# main # 
while running:
    for i in readNotes():
        content = i
        label = Label(window, text=i)
        label.pack()

    window.mainloop()