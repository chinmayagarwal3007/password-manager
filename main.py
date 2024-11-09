from tkinter import *
from tkinter import messagebox
import os
import random
from generate_password_func import generate_password_func
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


def add_func():

    website_name = website_input.get().strip()
    user_name = username_input.get().strip()
    password_value = password_input.get().strip()

    if(website_name == "" or user_name == "" or password_value == ""):
        messagebox.showwarning(message="One or more fields are empty!!")

    else:

        data = website_name + " | " + user_name + " | " + password_value

        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {user_name}\nPaaword: {password_value}\nIs it of to save?")


        if is_ok:
            new_data = {
                website_name:{
                    "user_name":user_name,
                    "password_value":password_value
                }
            }
            
            try:
                file = open("passwords.json", 'r')
            except FileNotFoundError:
                file = open("passwords.json", 'w')
                data = new_data
            else:
                try:
                    data = json.load(file)
                except:
                    data = new_data
                else:
                    data.update(new_data)
                finally:
                    file = open("passwords.json", 'w')
            finally:  
                json.dump(data, file, indent=4)
                file.close()

            # Clear the input fields after adding the entry
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo("Success", "Password saved successfully!")


def gen_pass():
    
    password_input.delete(0,END)
    passw = generate_password_func()
    pyperclip.copy(passw)
    password_input.insert(0, passw)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)


website = Label(text="Website")
website.grid(row=1,column=0)
username = Label(text="Email/Username")
username.grid(row=2,column=0)
password = Label(text="Password")
password.grid(row=3,column=0)


website_input = Entry()
website_input.grid(row=1, column=1,columnspan=2, sticky="EW")
website_input.focus()

username_input = Entry()
username_input.grid(row=2, column=1,columnspan=2, sticky="EW")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

generate_password = Button(text="Generate Paaword", command=gen_pass)
generate_password.grid(row=3, column=2, sticky="EW")

add_button = Button(width=35, text="Add", command=add_func)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")





window.mainloop()




