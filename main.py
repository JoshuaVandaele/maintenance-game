"""The main file for the program."""
# <========== Imports ==========>

import tkinter as tk

from Controller.MainMenuController import MainMenuController
from Controller.QuestionController import QuestionController

# <========== Main ==========>

if __name__ == "__main__":
    # Create some questions
    questions = QuestionController.generate_questions(10)

    controller = MainMenuController(questions)
    controller.root.mainloop()
