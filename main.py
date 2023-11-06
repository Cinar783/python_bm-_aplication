import tkinter
from tkinter import *

def button_funciton():
    print(weight_entry.get())


window=tkinter.Tk()
window.title("Pyhon BMI Aplication")
window.minsize(width=500,height=500)

weight_labale=Label(text='Enter Your Weight (kg)')
weight_labale.pack()

weight_entry=Entry()
weight_entry.pack()

height_label=Label(text='Enter Your Height (cm)')
height_label.pack()

height_entry=Entry()
height_entry.pack()

calculate_button=Button(text='Calculata',width=20,command=button_funciton)
calculate_button.config(pady=10)
calculate_button.pack()

label_conclusion=Label(text='Conclusion')
label_conclusion.pack()












tkinter.mainloop()