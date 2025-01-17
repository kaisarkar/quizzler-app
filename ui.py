from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg = "white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Some Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
         q_text = self.quiz.next_question()
         self.canvas.itemconfig(self.question_text, text=q_text)