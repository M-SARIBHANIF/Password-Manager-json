from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email":email,
        "password":password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Please dont leave any fields Empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- Search ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning!", message="No File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error",message="Website not saved")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pass Generation(Clipboard Enabled)")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)
website_label = Label(text="WebSite")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username/Tag")
email_label.grid(column=0,row=2)
password_Label = Label(text="Password")
password_Label.grid(column=0,row=3)
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=1)
website_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"Sample@email.com")
search_button = Button(text="Search",width=14 ,command=search)
search_button.grid(column=2,row=1)
password_entry = Entry(width=35)
password_entry.grid(column=1,row=3)
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2,row=3,columnspan=2)
save_button = Button(text="Save",width=46, command=save)
save_button.grid(column=1,row=4,columnspan=2)
window.mainloop()