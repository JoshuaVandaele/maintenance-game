# <========== Imports ==========>

from __future__ import annotations
import os
from pathlib import Path
from tkinter import Frame, PhotoImage, TclError, Tk

# <========== Local Imports ==========>

# Model Imports
from Model.Question import Question

# View Imports
from View.WelcomePage import WelcomePage

# Controller Imports
from Controller.QuestionController import QuestionController

# <========== Class ==========>

class MainMenuController:

    def __init__(self: MainMenuController, questions: list[Question]) -> None:
        """ The constructor for MainMenuController class.
        Create a view for the main menu.

        Args:
            self (QuestionController): Self.
            questions (list[Question]): All Questions to display when start button is pushed.
        """
        self.questions: list[Question] = questions

        self.root: Tk = Tk()
        self.root.title("Quiz Game")
        self.root.geometry("600x350")
        try:
            abs_path = os.getcwd() / Path("img/logo-favicon.png")
            self.root.iconphoto(False, PhotoImage(file=abs_path))
        except TclError:
            print("Warning: The favicon could not be loaded")
        self.views: Frame = WelcomePage(self.start, self.quit)
        self.views.pack()

    def start(self: MainMenuController) -> QuestionController:
        """ Start the main menu.

        Args:
            self (MainMenuController): Self.
        """
        self.root.destroy()
        return QuestionController(self.questions)

    def quit(self: MainMenuController) -> None:
        """ Quit the game.

        Args:
            self (MainMenuController): Self.
        """
        self.root.destroy()
