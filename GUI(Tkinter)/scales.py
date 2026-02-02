from tkinter import *

def submit():
    print("The Temperature is " + str(scale.get()))

root = Tk()
root.geometry("400x400") 

scale = Scale(root, from_=0, to=100,
              length=500,
              orient=VERTICAL, # horizontal or vertial
              font=('consoloas', 20),
              showvalue=0, #Hides current value
             tickinterval= 10,#adds numeric 
              resolution=5, # Increment of slider
              troughcolor="#69FAFF", #Chnages the color of slider
              bg='#111111', #changes the background color
              fg='#FF1C00' # chnages the foreground or text color
              )
scale.set((scale['to']- scale['from'])/2)
scale.pack()

button = Button(root, text="Submit", command=submit)
button.pack()



root.mainloop()