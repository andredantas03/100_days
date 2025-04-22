from tkinter import *
from tkinter import messagebox
import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Mypassword(Frame):
    def __init__(self, root = None):
        Frame.__init__(self, root, padx=20, pady=20)
        self.configure(bg="white")
        self.root = root
        self.grid()
        self.create_image()
        self.create_labels(text="Website:",column=0, row=1)
        self.create_labels(text=f"Email/Username: ", column=0, row=2)
        self.create_labels(text=f"Password: ", column=0, row=3)

        self.website_entry = self.create_entry(column=1,row=1,columnspan=3, focus=True, width=30)
        self.id_entry = self.create_entry(column=1,row=2,columnspan=3, width=30)
        self.password_entry = self.create_entry(column=1,row=3,columnspan=1, sticky="w",width=30)


        self.id_entry.insert(0, "seuemail@email.com")


        self.create_button(text="Generate Password", column=2, row=3, columnspan=1, func=self.generate_password)
        self.create_button(text="Add", column=1,row=4, columnspan=3, func=self.save_password)



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
        label_entry.grid(column=column, row=row, columnspan=columnspan, sticky=sticky)
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

        if len(web) == 0 or len(idstr) == 0 or len(passw) == 0:
            messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:"
                                                              f"\nEmail: {idstr} "
                                                              f"\nPassword: {passw}"
                                                              f"\nIs ok to save? ")
            if is_ok:
                with open("passwords.txt", "a") as file:
                    file.write(f"{web} | {idstr} | {passw}\n")
                    self.website_entry.delete(0, END)
                    self.id_entry.delete(0, END)
