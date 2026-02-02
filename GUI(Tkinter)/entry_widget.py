from tkinter import *
def submit():
    usernmae = entry.get()
    print(usernmae)

def delete():
    entry.delete(0,END)#deletes the line of text

def backspace():
    entry.delete(len(entry.get()) - 1, END)

root = Tk()
submit = Button(root,text='submit',command=submit)
submit.pack(side=RIGHT)

delete = Button(root,text='delete',command=delete)
delete.pack(side=RIGHT)

backspace = Button(root, text='backspace', command=backspace)
backspace.pack(side=RIGHT)

entry = Entry()
entry.config(font=('Ink Free', 50))
entry.config(bg='black')#Widget background is changed to the given color or hexadecimal value
entry.config(fg='green')#the text color in widget is changed to the given color or hexadecimale value 
# entry.insert(0,'shinchan')#A default given text is entered automatically 
# entry.config(state='readonly')
entry.config(width=10)#Width of the widget is changed to the given one 
# entry.config(show='*')#All the entered character as show the give * character
entry.pack()

root.mainloop()