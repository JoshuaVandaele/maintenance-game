"""Welcome Page module."""

# <========== Imports  ==========>

from __future__ import annotations

from tkinter import Button, Frame, Label, PhotoImage
from typing import Callable

# <========== Class  ==========>


class WelcomePage(Frame):
    """
    Representation of the Welcome Page
    """

    def __init__(self: WelcomePage, start_func: Callable, leave_func: Callable) -> None:
        super().__init__()

        self.image = PhotoImage(file="img/logo.png")
        self.image_label = Label(self, image=self.image)
        self.image_label.pack()

        self.start_func: Callable = start_func
        self.start_button = Button(
            self, text="Start the game", height=2, width=30, command=self.start
        )
        self.start_button.pack(pady=8)

        self.leave_func: Callable = leave_func
        self.quit_button = Button(
            self, text="Leave the game", height=2, width=30, command=self.leave
        )
        self.quit_button.pack(pady=8)

    def start(self: WelcomePage) -> None:
        """What to do when start button is pressed.

        Args:
            self (WelcomePage): Self.
        """
        self.start_func()

    def leave(self: WelcomePage) -> None:
        """What to do when leave button is pressed.

        Args:
            self (WelcomePage): Self.
        """
        self.leave_func()
