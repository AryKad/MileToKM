from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)


#entry
input = Entry()
input.focus()
input.grid(row=0, column= 1)

#label
milelabel = Label(text="Miles")
milelabel.grid(row=0, column=2)

equallabel = Label(text="is equal to")
equallabel.grid(row=1, column=0)

convert = Label(text="0")
convert.grid(row=1, column=1)

def con():
    val = float(input.get())
    convert.config(text=val*1.60934)

kmlabel = Label(text="KM")
kmlabel.grid(row=1, column=2)

#button
button = Button(text="Calculate", command=con)
button.grid(row=2, column=1)

window.mainloop()