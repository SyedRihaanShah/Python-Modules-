from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

root = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(root, text=food[index],
                               variable=x,
                               value=index,
                               padx = 25,
                               pady = 20,
                               font=('Impact', 50))
    radiobutton.pack(anchor=W)

root.mainloop()