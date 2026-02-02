from tkinter import *

root = Tk() 

root.geometry("420x420") # changes the dimensions of the current window
#Syntax : root.geometry(widthxheight±x±y)
#here x denotes horizontal postion and y reperesents vertical position of the window

root.title("Syed's Tkinter") #Changes the title of the current window

icon = PhotoImage(file="Demo.png") #This is used to change the iocn of the window
#syntax : name = PhotoImage(file='File_Name')
root.iconphoto(True, icon)
#Syntax : root.iconphoto(True/False, name)

root.config(background='yellow')#Used to change the color of the background 
#Syntax : root.onfig(background='Colorname or HexaDecimal Value)

message = Label(root, text='Hey there') # This is a widget 
message.pack() # to pack a widget
#General syntax of widget : widget = WidgetName(master, Keyword argument)
 
root.mainloop()

