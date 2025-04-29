import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.true_img = tk.PhotoImage(file='images/true.png')
        self.false_img = tk.PhotoImage(file='images/false.png')

        self.true_button = tk.Button(image=self.true_img,highlightthickness=0,command=self.true_pressed)
        self.false_button = tk.Button(image=self.false_img,highlightthickness=0,command=self.false_pressed)
        self.white_board = tk.Canvas(width=300,height=250,bg='white')
        self.question_text = self.white_board.create_text(150,125,
                                                          text="Some question text",
                                                          fill=THEME_COLOR,
                                                          font=("Arial", 20, "italic"),
                                                          width=280)
        self.score = tk.Label(text="Score: ",fg='white',bg=THEME_COLOR)

        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)
        self.white_board.grid(row=1,column=0, columnspan=2, pady=50)
        self.score.grid(row=0,column=1)



        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.white_board.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score.config(text = f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.white_board.itemconfig(self.question_text, text= q_text)
        else:
            self.white_board.itemconfig(self.question_text, text="Fim!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)
    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.white_board.config(bg="green")
        else:
            self.white_board.config(bg="red")
        self.window.after(1000,self.get_next_question)



