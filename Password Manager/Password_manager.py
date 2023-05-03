from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ------------------------- Search Password -------------------------------------------- #

def find_password():
    user_entry= website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data= json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="oops", message="You do not have this password saved")
    except KeyError:
        messagebox.showinfo(title="oops", message="You do not have this password saved")
    else:
        email = data[user_entry]["email"]
        password = data[user_entry]["password"]
        messagebox.showinfo(title=user_entry, message=f"Username: {email}\n "
                                                      f"Password: {password} ")






# ------------------------- Password Generator-------------------------------------------- #

#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(END, password)
    pyperclip.copy(password)


# ------------------------- Save Password-------------------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data= {
        website: {
            "email" : email,
            "password": password
                  }
    }

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="oops", message="Hey! It seems like you have left some fields empty."
                                                            "\n Please fill and then add")

    else:
        is_ok = messagebox.askyesno(title= website, message=f"This is all the info to be saved:\n \n "
                                                    f"Email: {email}\n Password: {password}\n \n Is it okay to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0,END)



# ------------------------- UI Setup-------------------------------------------- #

#Window
window= Tk()
window.title("My Password Manager")
window.config(padx=40, pady=40)

#Canvas
canvas = Canvas(height= 200, width = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_id_label  = Label(text= "Email Id/Username: ")
email_id_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#Entries

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "tayalpushpal@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=12, command= find_password)
search_button.grid(row=1, column=2)

window.mainloop()

