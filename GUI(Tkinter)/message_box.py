from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is an info message box", message='You are a person')
    # messagebox.showwarning(title='WARNING', message='You have a virus')
    # messagebox.showerror(title='Error', message='Something went wrong')
    # if messagebox.askokcancel(title='Ask ok cancel', message="Do you want to do the thing"):
    #     print("You did the thing")
    # else:
    #     print("You cancelled the thing :(")

    # if messagebox.askretrycancel(title="retry or cancel", message="Do yo want to retry"):
    #     print("you retried a thiing")
    # else:
    #     print("You cancelled a thing")

    # if messagebox.askyesno(title="Ask yes or no", message="Do you like food?"):
    #     print("I like food")
    # else:
    #     print("Why dont you like food?")

    # asnwer = messagebox.askquestion(title="ask question", message="Do you like pizza?") # retrns 'yes' or 'no'
    # if asnwer =='yes':
    #     print('I like pizza too')
    # else:
    #     print('You don like piza bruh -_-')

    answer = messagebox.askyesnocancel(title='YES NO CANCEL', message='Do you like to code?')#returns True False None

    if answer == True : 
        print("I like to code too !")
    elif answer == False :
        print("Sad you dont like to code ;-;")
    else:
        print("You cancelled the program")

root = Tk()

button = Button(root, command=click, text= "click me")
button.pack()

root.mainloop()