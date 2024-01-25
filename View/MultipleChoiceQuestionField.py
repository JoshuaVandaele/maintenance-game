# <========== Imports ==========>

from __future__ import annotations
from tkinter import Frame, Label, StringVar, Radiobutton, Button
from typing import Callable
from random import shuffle

# <========== Class ==========>

class MultipleChoiceQuestionField(Frame):
    """ Class representing a frame displaying a multiple choice question,
    it contains a label, radio buttons (representing answer possibility) and a submit button.
    Derived from tkinter Frame.
    """

    def __init__(self: MultipleChoiceQuestionField, label_text: str, choices: list[str], submit_func: Callable) -> None:
        """ Constructor for a frame displaying a multiple choice question

        Args:
            self (MultipleChoiceQuestionField): Self.
            label_text (str): The text question using to display.
            choices (list[str]): All possibility (answer + traps)
            submit_func (Callable): What to do when submit button is pressed
        """
        shuffle(choices)

        super().__init__()

        self.label: Label = Label(self, text=label_text)
        self.label.grid(row=0, column=0, columnspan=len(choices))
        self.radio_buttons: list[Radiobutton] = []
        self.radio_button_variable: StringVar = StringVar(value=choices[0])
        self.submit_func: Callable = submit_func

        for i, choice in enumerate(choices):
            radio_button: Radiobutton = Radiobutton(self, text=choice, variable= self.radio_button_variable, value=choice)
            radio_button.grid(row=1, column=i)
            self.radio_buttons.append(radio_button)

        self.submit_button: Button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=len(choices))

    def submit(self: MultipleChoiceQuestionField) -> None:
        """ What to do when submit button is pressed.

        Args:
            self (MultipleChoiceQuestionField): Self.
        """
        self.submit_func(self.radio_button_variable.get())