from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir='/Users/syedrihaanshah/Python-Modules-/GUI(Tkinter)',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text file", "*.txt"),
                                        ("HTML", "*.html"),
                                        ("all files", ".*")
                                    ])
    textfile = str(text.get(1.0, END))
    file.write(textfile)
    file.close()

root = Tk()

button = Button(root, text= "Save As", command=savefile)
button.pack()
text = Text(root)
text.pack()

root.mainloop()