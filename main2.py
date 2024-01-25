# <========== Imports ==========>

import tkinter as tk

from Controller.QuestionController import QuestionController
from Controller.MainMenuController import MainMenuController

# <========== Main ==========>

if __name__ == "__main__":
    # Create some questions
    questions =[]

    controller = MainMenuController(questions)
    controller.root.mainloop()
