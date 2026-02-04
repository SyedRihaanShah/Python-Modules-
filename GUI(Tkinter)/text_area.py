#text widget = functions like a text area, you can enter multiple lines of text 
from tkinter import *

def Submit():
    input = text.get('1.0', END)
    print(input)
root = Tk()

text = Text(root,
            background='light yellow',
            font=('ink free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()

button = Button(root, command=Submit, text='submit' )
button.pack()

root.mainloop()