# <========== Imports ==========>

import tkinter as tk

from Controller.QuestionController import QuestionController
from Controller.MainMenuController import MainMenuController

from Model.OpenQuestion import OpenQuestion
from Model.MultipleChoiceQuestion import MultipleChoiceQuestion

# <========== Main ==========>

if __name__ == "__main__":
    # Create some questions
    questions = [QuestionController.generate_questions(10)]

    controller = MainMenuController(questions)
    controller.root.mainloop()
