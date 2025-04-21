from tkinter import *
from tkinter import messagebox
import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    char_list = letters+numbers+symbols
    gen_password = [i for i in random.choices(char_list,k=12)]
    password = "".join(gen_password)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    idstr = id_entry.get()
    passw = password_entry.get()

    if len(web) == 0 or len(idstr) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:"
                                                             f"\nEmail: {idstr} "
                                                             f"\nPassword: {passw}"
                                                             f"\nIs ok to save? ")
        if is_ok:
            with open("passwords.txt","a") as file:
                file.write(f"{web} | {idstr} | {passw}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("My Password")
root.config(padx=50,pady=50)

mainframe = Frame(root)
mainframe.grid(column=0,row=0)

canvas = Canvas(mainframe, width=200,height=200)
img = PhotoImage(master=canvas,file="logo.png")

canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website = Label(mainframe,text="Website: ")
website.grid(column=0,row=1,sticky="w")
website_entry = Entry(mainframe,width=23)
website_entry.grid(column=1,row=1,columnspan=3,sticky="w e")
website_entry.focus()


id = Label(mainframe,text="Email/Username: ")
id.grid(column=0,row=2,sticky="w")
id_entry = Entry(mainframe,width=23)
id_entry.grid(column=1,row=2,columnspan=3,sticky="w e")
id_entry.insert(0,"seuemail@email.com")


password = Label(mainframe,text="Password: ")
password.grid(column=0,row=3,sticky="w")
password_entry = Entry(mainframe,width=21)
password_entry.grid(column=1,row=3,columnspan=2,sticky="w")

generate = Button(mainframe,text="Generate Password",command=generate_password)
generate.grid(column=2,row=3,sticky="w e")

add = Button(mainframe,text="Add", command=generate_password)
add.grid(column=1,row=4, columnspan=3,sticky="w e")



root.mainloop()