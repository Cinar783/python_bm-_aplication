import tkinter

window=tkinter.Tk()
window.title("Python Tkinter BMI Calculator")
window.config(pady=20,padx=20)
window.minsize(500,500)

def button_function():
    height=height_entry.get()
    weight=weight_entry.get()
    if height=='' or weight=='':
        result_label.config(text='Please enter height and weight')
    else:
        bmı=float(weight)/(float(height)/100)**2
        result_string=write_resutl(bmı)
        result_label.config(text=result_string)


#ui
height_label=tkinter.Label(text='Please Enter Height (cm)',font='italic')
height_label.pack()

height_entry=tkinter.Entry()
height_entry.pack()


weigth_label=tkinter.Label(text='Please Enter Weight (kg)',font='italic',pady=20)
weigth_label.pack()

weight_entry=tkinter.Entry()
weight_entry.pack()

calculate_button=tkinter.Button(text='Calculate',font='italic',command=button_function)
calculate_button.pack()


result_label=tkinter.Label()
result_label.pack()


def write_resutl(bmi):
    result_string=(f'You are BMI {round(bmi,2)} You are ')
    if bmi<=18.5:
        result_string+='Thin'
    elif bmi>=18.6 and bmi<=24.90:
        result_string+='Healty'
    elif bmi>=25 and bmi<=29.9:
        result_string+='Overweight'
    else:
        result_string+='Obese'
    return result_string

tkinter.mainloop()