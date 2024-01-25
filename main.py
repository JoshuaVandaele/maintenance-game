# <========== Imports ==========>

import tkinter as tk

# <========== Local Import ==========>

from Model.OpenQuestion import OpenQuestion
from Model.MultipleChoiceQuestion import MultipleChoiceQuestion
from Controller.QuestionController import QuestionController
from Controller.MainMenuController import MainMenuController

# <========== Main ==========>

if __name__ == "__main__":
    # Create some questions
    questions = [
        OpenQuestion("What is the capital of France?", ["Paris"]),
        MultipleChoiceQuestion("What is the capital of Germany?", ["D"], ["A", "B", "C", "E", "F", "G", "H"]),
        OpenQuestion("What is the capital of Italy?", ["Rome"]),
    ]

    # Create a QuestionController
    controller = MainMenuController(questions)
    controller.root.mainloop()