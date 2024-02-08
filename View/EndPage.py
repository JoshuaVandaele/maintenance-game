# <========== Imports  ==========>

from __future__ import annotations
from tkinter import Frame, Button, Label, PhotoImage, Text
from typing import Callable

# <========== Class  ==========>

class EndPage(Frame):
    """
    Representation of the Welcome Page
    """
    def __init__(self: EndPage, start_func: Callable, leave_func: Callable) -> None:
        super().__init__()

        self.image = PhotoImage(file="img/logo.png")
        self.image_label = Label(self, image=self.image)
        self.image_label.pack()
        self.text = Label(self, text="Bravo! Vous avez terminé cette partie", font=("Helvetica", 50))
        self.text.pack(anchor='center')


    def start(self: EndPage) -> None:
        """ What to do when start button is pressed.

        Args:
            self (EndPage): Self.
        """
        self.start_func()

    def leave(self: EndPage) -> None:
        """ What to do when leave button is pressed.

        Args:
            self (EndPage): Self.
        """
        self.leave_func()