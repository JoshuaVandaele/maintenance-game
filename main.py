# <========== Imports ==========>

import tkinter as tk

from Controller.QuestionController import QuestionController
from Model.MultipleChoiceQuestion import MultipleChoiceQuestion
from Model.OpenQuestion import OpenQuestion

# <========== Main ==========>

if __name__ == "__main__":
    # Create some questions
    questions = QuestionController.generate_questions(10)

    # Create a QuestionController
    question_controller = QuestionController(questions)

    question_controller.root.mainloop()
