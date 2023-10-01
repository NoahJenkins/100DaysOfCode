from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Windows Set up
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

#Canvas (Image) Set Up
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)

#Website Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

#Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
 
#Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
 
#Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
 
#Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Password Entry
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1, sticky=EW)
 
#Generate Password Button
generate_password_but = Button(text="Generate Password")
generate_password_but.grid(row=3, column=2, sticky=EW)
 
#Add Button
add_password_but = Button(text="Add", width=30)
add_password_but.grid(row=4, column=1, columnspan=2, sticky=EW)



window.mainloop()

