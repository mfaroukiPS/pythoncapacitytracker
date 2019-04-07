from tkinter import *
from tkinter.ttk import *
from loads import getcollaborator

window = Tk()
window.geometry('200x200')
window.title('Team charge')

#creating 2 frames Top and Bottom
top_frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = "bottom")


# combo = Combobox(top_frame).pack()
combo['values'] = getcollaborator()
combo['values']=(1,2,3,3)


window.mainloop()