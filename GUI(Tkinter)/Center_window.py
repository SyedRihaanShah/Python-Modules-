from tkinter import *

root = Tk()
root.title("CenterScreen")

window_width = 300
window_length = 200

screen_width = root.winfo_screenwidth()#gets the screen widhth in pixels
screen_length = root.winfo_screenheight()#gets the screen lenght in pixels

center_X = int(screen_width/2 - window_width/2)
center_y = int(screen_length/2 - window_length/2)

root.geometry(f"{window_width}x{window_length}+{center_X}+{center_y}")

root.mainloop()