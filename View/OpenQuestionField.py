"""Open Question Field Module"""

# <========== Imports ==========>

from __future__ import annotations

from tkinter import Button, Entry, Frame, Label
from typing import Callable

# <========== Class ==========>


class OpenQuestionField(Frame):
    """ Class representing a frame displaying an open question,
    it contains a label, an entry and a submit button.
    Derived from tkinter Frame.
    """

    def __init__(self: OpenQuestionField, label_text: str, submit_func: Callable) -> None:
        """ Constructor for a frame displaying an open question

        Args:
            self (OpenQuestionField): Self.
            label_text (str): The text question used for display.
            submit_func (Callable): What to do when submit button is pressed
        """
        super().__init__()
        self.submit_func: Callable = submit_func

        # Configure le fond du frame
        self.configure(bg="#383838")

        self.label: Label = Label(self, text=label_text, font=('Times New Roman', 20), bg="#383838", fg="white")
        self.label.pack(pady=15)

        self.entry: Entry = Entry(self, width=40, fg="black")
        self.entry.pack()

        self.submit_button = Button(self, text="Submit", command=self.submit, width=20, height=2, bg="#343434", fg="white")
        self.submit_button.pack(pady=15)

    def submit(self: OpenQuestionField) -> None:
        """What to do when submit button is pressed.

        Args:
            self (OpenQuestionField): Self.
        """
        self.submit_func(self.entry.get())
