from tkinter import *

root = Tk()

photo = PhotoImage(file='Demo.png')
text_label = Label(root,text='Hello Whats up? How are you',
                    font=('Arial',40, 'bold'),#font releated arguments are passed 
                    fg="Red", #font color  
                    bg='black',#back ground color 
                    relief=RAISED,#border 
                    bd=10,#border width
                    padx=20,#padding in x 
                    pady=30,#padding in y
                    image=photo,#image is added
                    compound='top')#image is top of the text
text_label.pack() #Or you can use the bottom one too
# text_label.place(x=0, y=0)

root.mainloop()

#lables = an area widget that holds text and/or image within a window