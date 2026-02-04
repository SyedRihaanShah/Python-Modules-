from tkinter import * 


def openfile():
    print("File has been opened")

def SaveFile():
    print("File has been Saved")
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='open',command=openfile)
filemenu.add_command(label='open', command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label='exit',command=quit)

root.mainloop()