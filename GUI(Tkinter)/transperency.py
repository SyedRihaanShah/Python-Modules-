from tkinter import *

root  = Tk()

root.geometry("300x500")
widget = Label(text='Hey there', font=('ARIAL', 35))
widget.pack()

root.attributes('-alpha', 0.5)
#syntax : root.attributes('-alpha', "A number between 1.0 and 0.0")
#1.0 = fully opqaue and 0.0 = fully transparent

root.mainloop()