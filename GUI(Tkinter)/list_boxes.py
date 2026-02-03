from tkinter import *

def submit():
    print("You have ordered ")
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entrbox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
root = Tk()
root.geometry("500x500")

listbox = Listbox(root,
                  bg = '#F7FFDD',
                  font=('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE #We can select multiple options at once 
                  )
listbox.pack()

listbox.insert(1, 'Biryani')
listbox.insert(2, "Tandoori")
listbox.insert(3, "Lassi")
listbox.insert(4, "Kebab")

entrbox = Entry(root)
entrbox.pack()

listbox.config(height=listbox.size())

addbutton = Button(root, text='add',command=add)
addbutton.pack()
deletebutton = Button(root, text='delete', command=delete)
deletebutton.pack()
submitbutton = Button(root,text="Submit", command=submit)
submitbutton.pack()

root.mainloop()