from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_pass = [choice(letters) for char in range(randint(8, 10))]
    numbers_pass = [choice(numbers) for char in range(randint(2, 4))]
    symbol_pass = [choice(symbols) for char in range(randint(2, 4))]

    password_list = letters_pass + numbers_pass + symbol_pass

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #Using get function to get current text in entry boxes
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Warning", message="Please fill out any empty fields.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the credentials entered: \nEmail: {email}\nPassword: {password}\nAre you sure you want to save?")

        if is_okay:
            with open("data.txt", "a") as dat_file:
                dat_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry.focus() 

#Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
 
#Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "first.last@domain.com")
 
#Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Password Entry
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1, sticky=EW)
 
#Generate Password Button
generate_password_but = Button(text="Generate Password", command=generate_password)
generate_password_but.grid(row=3, column=2, sticky=EW)
 
#Add Button
add_password_but = Button(text="Add", width=30, command=save)
add_password_but.grid(row=4, column=1, columnspan=2, sticky=EW)



window.mainloop()

