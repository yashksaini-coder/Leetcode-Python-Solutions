import tkinter as tk

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.questions = self.load_questions()
        self.total_questions = len(self.questions)
        self.current_question = 0
        self.correct_answers = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=20)

        self.answer_label = tk.Label(root, text="", font=("Arial", 12))
        self.answer_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def load_questions(self):
        questions = []
        with open("questions.txt", "r") as file:
            lines = file.readlines()
            question = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Question"):
                    if question:
                        questions.append(question)
                        question = {}
                    question["text"] = line
                elif line.startswith("Correct Answer"):
                    question["answer"] = line.split(":")[1].strip().lower()
                elif line.startswith(("a)", "b)", "c)", "d)")):
                    option, text = line.split(")", 1)
                    question[option.strip().lower()] = text.strip()
            if question:
                questions.append(question)
        return questions


    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["text"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for option in question:
            if option != "text" and option != "answer":
                button = tk.Button(self.options_frame, text=f"{option.upper()}. {question[option]}",
                                   command=lambda option=option: self.check_answer(option))
                button.pack(pady=5)

    def check_answer(self, selected_option):
        question = self.questions[self.current_question]
        correct_answer = question["answer"]

        if selected_option == correct_answer:
            self.correct_answers += 1
            self.answer_label.config(text="Correct!", fg="green")
        else:
            self.answer_label.config(text="Incorrect!", fg="red")

        self.next_button.config(state=tk.NORMAL)

        for widget in self.options_frame.winfo_children():
            widget.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1

        if self.current_question < self.total_questions:
            self.display_question()
            self.next_button.config(state=tk.DISABLED)
            self.answer_label.config(text="")
        else:
            self.show_report()

    def show_report(self):
        report = f"Number of questions asked: {self.total_questions}\n"
        report += f"Number of questions answered correctly: {self.correct_answers}"

        self.question_label.config(text="Quiz Completed!")
        self.answer_label.config(text=report)
        self.next_button.config(text="Exit", command=self.root.quit)

root = tk.Tk()
root.title("Quiz Application")
app = QuizApplication(root)
root.mainloop()
