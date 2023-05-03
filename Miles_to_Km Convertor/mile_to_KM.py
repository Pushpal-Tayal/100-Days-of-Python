from tkinter import *

#window

window = Tk()
window.title("Mile to Km convertor")
window.minsize(width=500, height=100)
#canvas- To place something on 0,0

canvas = Canvas(height=10, width=70)
canvas.grid(row=0, column=0)

#Entry

entry = Entry(width=50)
entry.insert(END, string= "0")
user_input= entry.get()
entry.grid(row=0, column=1)

#label-Miles

label = Label(text="miles", font=("Arial", 10))
label.grid(row=0, column=2)

#label-is equal to

label_1 = Label(text= "is equal to", font=("Arial", 10))
label_1.grid(row=1, column=0)

#label-Km

label_2 = Label(text= "Km", font=("Arial", 10))
label_2.grid(row=1, column=2)

#label-calculated value
calculated_value= round(float(user_input) * 10)
label_3 = Label(font=("Arial", 10))
label_3.grid(row=1, column=1)

#button-calculate
def button_clicked():
    label_3.config(text= f"{calculated_value}")

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
