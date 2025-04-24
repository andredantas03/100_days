from tkinter import *
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"

class Flashcard(Frame):
    def __init__(self, root = None):
        super().__init__(master=root)
        self.root = root
        self.config(bg=BACKGROUND_COLOR)
        self.root.config(bg=BACKGROUND_COLOR)
        self.grid(padx=50,pady=50)

        self.card_front = self.image_creator(width=800,height=526,
                                             file="images/card_front.png",
                                             x=400,y=283)
        self.card_front["canvas"].grid(column=0,row=0,columnspan=2)
        self.card_front["canvas"].create_text(400,150,text="Title", font=("Ariel",40,"italic"))
        self.card_front["canvas"].create_text(400,263,text="word", font=("Ariel",60,"bold"))






        self.right = self.image_creator(width=100, height=100,
                                             file="images/right.png",
                                             x=50, y=50)
        self.right["canvas"].bind("<Button-1>", click)
        self.right["canvas"].grid(column=0, row=1, columnspan=1)

        self.wrong = self.image_creator(width=100, height=100,
                                             file="images/wrong.png",
                                             x=50, y=50)
        self.wrong["canvas"].bind("<Button-1>", click)
        self.wrong["canvas"].grid(column=1, row=1, columnspan=1)




    def image_creator(self,width,height,file,x,y):
        area = Canvas(self, width=width, height=height,
                                bg=BACKGROUND_COLOR, highlightthickness=0)
        img = PhotoImage(file=file)
        area.create_image(x, y, image=img)
        return {"canvas":area,"img":img}
