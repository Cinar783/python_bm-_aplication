import tkinter
from tkinter import *

window=tkinter.Tk()
window.title("Python BMI Tkinter")
window.minsize(500,500)
calculate=0

def buttton_function():
    height=entry_height.get()
    weight=entry_weight.get()
    if weight=="" or height=="":
        my_calculate.config(text="Boy ve Kilo giriniz")
    else:
        try:
            calculate=(float(weight)/(float(height)/100)**2)
            my_calculate.config(text=f'Vicut İndeksiniz: {calculate}')
            if calculate<18.5:
                message_calculate.config(text='Düşük Kilolusunuz')
            elif calculate>=18.50 and calculate<=24.99:
                message_calculate.config(text='Normal Kilolusunuz')
            elif calculate>=25.00 and calculate<=29.99:
                message_calculate.config(text='Fazla Kilolusunuz')
            elif calculate>=30.00:
                message_calculate.config(text='Obezsiniz')

        except:
            my_calculate.config(text='Rakam Giriniz')


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


my_button=Button(text='Calculate',padx=20,font='italic',command=buttton_function)
my_button.pack()

my_calculate=Label(text='Calculate')
my_calculate.pack()

message_calculate=Label(text='Message Calculate')
message_calculate.pack()






window.mainloop()