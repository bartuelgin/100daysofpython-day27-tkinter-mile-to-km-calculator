from tkinter import *

window = Tk()
window.title("From Mile to Km Converter")
window.minsize(width=300 , height=300)
window.config(padx= 20, pady=20)

#Entry for user mile input
entry = Entry()
entry.insert(END, string="Enter Mile Here")
entry.grid(row=0 ,column= 1)


#text label for miles
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)
label_miles.config(padx= 20, pady=20)

#label for "is equal to"
label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)
label_is_equal.config(padx= 20, pady=20)

#label for "KM calculation"
label_km = Label(text="0")
label_km.grid(row=1, column=1)
label_km.config(padx= 20, pady=20)

#label for "KM"
label_is_text_KM = Label(text="KM")
label_is_text_KM.grid(row=1, column=2)

#Button for Calculate


def calculate():
    user_input = int(entry.get())
    km = user_input * 1.6
    label_km["text"] = km


button = Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)





window.mainloop()