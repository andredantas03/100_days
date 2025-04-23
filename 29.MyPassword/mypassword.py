from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Mypassword(Frame):
    def __init__(self, root = None):
        super().__init__(root, padx=20, pady=20)
        self.configure(bg="white")
        self.root = root
        self.grid()
        self.create_image()
        self.create_labels(text="Website:",column=0, row=1)
        self.create_labels(text=f"Email/Username: ", column=0, row=2)
        self.create_labels(text=f"Password: ", column=0, row=3)

        self.website_entry = self.create_entry(column=1,row=1,columnspan=2, focus=True, width=30,sticky="w")
        self.id_entry = self.create_entry(column=1,row=2,columnspan=3, width=30)
        self.password_entry = self.create_entry(column=1,row=3,columnspan=1, sticky="w",width=30)


        self.id_entry.insert(0, "seuemail@email.com")


        self.create_button(text="Generate Password", column=2, row=3, columnspan=1, func=self.generate_password)
        self.create_button(text="Add", column=1,row=4, columnspan=3, func=self.save_password)
        self.create_button(text="Search", column=2,row=1, columnspan=1, func=self.search)



    def create_image(self):
        self.myphoto = PhotoImage(file = 'logo.png')
        self.canvas = Canvas(self,width=200,height=200)
        self.canvas.create_image(100,100,image = self.myphoto)
        self.canvas.grid(column=1,row=0)

    def create_labels(self,column=0,row=0,text=""):
        label = Label(self, text=text)
        label.grid(column=column, row=row, sticky="w")

    def create_entry(self, column, row, columnspan,sticky="w e", focus=False, width=30):
        label_entry = Entry(self, width=width)
        label_entry.grid(column=column,pady=3, row=row, columnspan=columnspan, sticky=sticky)
        if focus:
            label_entry.focus()
        return label_entry

    def create_button(self,text, column, row,columnspan, func):
        button = Button(self, text=text, command=func)
        button.grid(column=column, row=row, columnspan=columnspan, sticky="w e")

    def generate_password(self):
        char_list = letters + numbers + symbols
        gen_password = [i for i in random.choices(char_list, k=12)]
        password = "".join(gen_password)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)


    def save_password(self):
        web = self.website_entry.get()
        idstr = self.id_entry.get()
        passw = self.password_entry.get()
        new_data = {
            web:{
                "email/username":idstr,
                "password":passw
            }
        }

        if len(web) == 0 or len(idstr) == 0 or len(passw) == 0:
            messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty!")
        else:
            try:
                with open("passwords.json", "r") as file:
                    #reading old data
                    data = json.load(file)
            except FileNotFoundError:
                #creating new json file in case it doesn't exist
                self.write_file(new_data)
            else:
                #updating old data with new data
                data.update(new_data)
                #saving data
                self.write_file(data)

            finally:
                #clean the entries
                self.password_entry.delete(0, END)
                self.website_entry.delete(0, END)


    def write_file(self,new_data,file="passwords.json"):
        with open(file, "w") as file:
            data = json.dump(new_data, file, indent=4)

    def search(self):
        website = self.website_entry.get()
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
            idstr = data[website]['email/username']
            passw = data[website]['password']
            messagebox.showinfo(title="Password Founded!",
                                message=f"Password was funded. \nId: {idstr} \nPassword: {passw}")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="There's no such file.")
        except KeyError:
            messagebox.showinfo(title="Oops!", message="There's no password saved for this website.")
