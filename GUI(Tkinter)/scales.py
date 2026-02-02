from  tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + "degressC")

root = Tk()
scale = Scale(root,
              from_=0, to= 100,
              length=500,
              orient=VERTICAL,#orientation of the scale
              font=("Consolas",20),
              tickinterval=10,#this adds numeric indicators
              showvalue=0,#hide current value
              resolution=5,#increment of slider
              troughcolor='#69FAFF',
              fg='red',
              bg='black')
scale.set((scale['from'] - scale['to'])/2 + (scale['to']))
scale.pack()

button = Button(root,text='Submit',command=submit)
button.pack()
root.mainloop()