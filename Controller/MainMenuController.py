"""The main menu controller file for the program."""
# <========== Imports ==========>

from __future__ import annotations

import os
from pathlib import Path
from tkinter import Frame, PhotoImage, TclError, Tk

# Controller Imports
from Controller.QuestionController import QuestionController

# Model Imports
from Model.Question import Question

# View Imports
from View.WelcomePage import WelcomePage

# <========== Local Imports ==========>


# <========== Class ==========>


class MainMenuController:
    """Controller using to manage the main menu."""

    def __init__(self: MainMenuController, questions: list[Question]) -> None:
        """The constructor for MainMenuController class.
        Create a view for the main menu.

        Args:
            self (QuestionController): Self.
            questions (list[Question]): All Questions to display when start button is pushed.
        """
        self.questions: list[Question] = questions

        self.root: Tk = Tk()
        self.root.title("Quiz Game")
        self.root.configure(background="#383838")
        try:
            abs_path = os.getcwd() / Path("img/logo-favicon.png")
            self.root.iconphoto(False, PhotoImage(file=abs_path))
        except TclError:
            print("Warning: The favicon could not be loaded")
        self.views: Frame = WelcomePage(self.start, self.quit)
        self.views.pack()

        self.root.resizable(False, False)

    def start(self: MainMenuController) -> QuestionController:
        """Start the main menu.

        Args:
            self (MainMenuController): Self.
        """
        self.root.destroy()
        return QuestionController(self.questions)

    def quit(self: MainMenuController) -> None:
        """Quit the game.

        Args:
            self (MainMenuController): Self.
        """
        self.root.destroy()
