from tkinter import *

#Command/Calculation
def calculate():
   miles = float(miles_entry.get())
   kilo_m = miles * 1.6
   kilometers = round(kilo_m, 2)
   km_entry.config(text= f'{kilometers} Km')


#Create Window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)

#Equal label
equal_label = Label(text='is equal to')
equal_label.grid(column=0, row =1)

#Miles Label
miles_label = Label(text="Mile")
miles_label.grid(column=2, row =0)

#Miles Label
km_label = Label(text="Km")
km_label.grid(column=2, row =1)

#Miles Entry
miles_entry = Entry()
miles_entry.grid(column=1, row =0)
miles_entry.get()

#Answer Label
km_entry = Label()
km_entry.grid(column=1, row =1)


#Calc Button
calc_button = Button(text="calculate", command= calculate)
calc_button.grid(column=1, row=2)





















window.mainloop()