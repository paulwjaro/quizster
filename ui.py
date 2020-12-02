from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, first_question, quiz):
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizster")
        self.score_board = Label(text="Score: 0")
        self.score_board.config(bg=THEME_COLOR, fg="white", font=("arial", 20, "bold"))
        self.score_board.grid(row=0, column=1, padx=20, pady=10)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 100, width=250, text=f"Q.1: {first_question}",
                                                     font=("Arial", 16, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.true_img = None
        self.false_img = None
        self.true_button = None
        self.false_button = None
        self.current_quiz = quiz

    def create_buttons(self):
        self.true_img = PhotoImage(file="true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

    def true_pressed(self):
        next_question = self.current_quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=f"Q.{self.current_quiz.question_number}: {next_question}")
        if self.current_quiz.question_number < len(self.current_quiz.question_list):
            self.current_quiz.check_answer("true")
            self.score_board.config(text=f"Score: {self.current_quiz.score}")

    def false_pressed(self):
        next_question = self.current_quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=f"Q.{self.current_quiz.question_number}: {next_question}")
        if self.current_quiz.question_number < len(self.current_quiz.question_list):
            self.current_quiz.check_answer("false")
            self.score_board.config(text=f"Score: {self.current_quiz.score}")
