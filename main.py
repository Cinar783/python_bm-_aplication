import tkinter
from tkinter import *

window=tkinter.Tk()
window.title("Python BMI Tkinter")
window.minsize(500,500)

#Boy
label_height=Label(text='Please Enter Height',font='italic',pady=10)
label_height.pack()

entry_height=Entry(bg='light blue',font='italic')
entry_height.pack()


#kilo
label_weight=Label(text='Please Enter Weight',font='italic',pady=20)
label_weight.pack()


entry_weight=Entry(bg='light blue',font='italic')
entry_weight.pack()


my_button=Button(text='Calculate',padx=20,font='italic')
my_button.pack()



window.mainloop()