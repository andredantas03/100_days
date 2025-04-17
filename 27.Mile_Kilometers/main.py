from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize()
miles = "0"

def calculate():
    a = input.get()
    text["text"] = round(float(a)*1.41,2)

input = Entry(width=5)
input.insert("1",miles)
input.grid(row=0,column=1)

label1 = Label(text="Miles")
label1.grid(row=0,column=2)

label2 = Label(text = "Is equal to")
label2.grid(row=1,column=0)

label3 = Label(text="Km")
label3.grid(row=1,column=2)

button = Button(text="Calculate",command=calculate)
button.grid(row=2,column=1)

text = Label(text=miles)
text.grid(row=1,column=1)


window.mainloop()