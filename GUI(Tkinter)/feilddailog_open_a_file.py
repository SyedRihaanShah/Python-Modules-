from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfile(initialdir="/Users/syedrihaanshah/Python-Modules-", title="Open File ",
                                      filetypes=(("text files",'*.txt' ),("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

root = Tk()

button = Button(root, text='To Open', command=openfile)
button.pack()

root.mainloop()