from tkinter import *

def click():
    print("Hello")
root = Tk()
button = Button(root, text='Click me!')
button.pack()
button.config(command=click)
button.config(font=('Ink Free', 45, 'bold'))
button.config(bg='Orange')
button.config(fg="red")
button.config(activebackground='blue')
button.config(activeforeground='pink')
image = PhotoImage(file='demo.png')
button.config(image=image)
button.config(compound='top')
button.config(state="disabled")
root.mainloop()