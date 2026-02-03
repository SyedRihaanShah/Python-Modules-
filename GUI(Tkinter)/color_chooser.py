from tkinter import *
from tkinter import colorchooser #submodule 

def click():
    # color = colorchooser.askcolor()
    # colorhex = color[1]
    # root.config(bg=colorhex)
    root.config(bg=colorchooser.askcolor()[1])


root = Tk()

root.geometry('420x420')
button = Button(root, text='Click Me', command=click)
button.pack()

root.mainloop()