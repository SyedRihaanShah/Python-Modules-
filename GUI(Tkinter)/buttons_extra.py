from tkinter import *

count = 0

def click():
    global count
    count += 1
    label.config(text=count)
    label2.pack()
    
root = Tk()
root.config(background='yellow')
button = Button(root, text='Click me!')
button.pack()
button.config(command=click)
button.config(font=('Ink Free', 45, 'bold'))
button.config(bg='Orange')
button.config(fg="red")
button.config(activebackground='blue')
button.config(activeforeground='pink')
image = PhotoImage(file='Demo.png')
button.config(image=image)
button.config(compound='top')
button.config(state="active")
label = Label(root, text=count )
label.config(font=('Monospace', 25))
label.pack()
label2 = Label(root, image=image)
root.mainloop()