"""Open Question Field Module"""

# <========== Imports ==========>

from __future__ import annotations

from tkinter import Button, Entry, Frame, Label
from typing import Callable

# <========== Class ==========>


class OpenQuestionField(Frame):
    """Class representing a frame displaying a open question,
    it contains a label, an entry and a submit button.
    Derived from tkinter Frame.
    """

    def __init__(
        self: OpenQuestionField, label_text: str, submit_func: Callable
    ) -> None:
        """Constructor for a frame displaying a open question

        Args:
            self (OpenQuestionField): Self.
            label_text (str): The text question using to display.
            submit_func (Callable): What to do when submit button is pressed
        """
        super().__init__()
        self.submit_func: Callable = submit_func

        self.label: Label = Label(self, text=label_text)
        self.label.pack()

        self.entry: Entry = Entry(self)
        self.entry.pack()

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self: OpenQuestionField) -> None:
        """What to do when submit button is pressed.

        Args:
            self (OpenQuestionField): Self.
        """
        self.submit_func(self.entry.get())
