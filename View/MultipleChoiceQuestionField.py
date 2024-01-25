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

        self.configure(bg="#383838")

        self.label: Label = Label(self, text=label_text, font=('Times New Roman', 20), bg="#383838", fg="white")
        self.label.grid(row=0, column=0, columnspan=len(choices), pady=15)  # Ajout de pady=15 ici
        self.radio_buttons: list[Radiobutton] = []
        self.radio_button_variable: StringVar = StringVar(value=choices[0])
        self.submit_func: Callable = submit_func

        for i, choice in enumerate(choices):
            radio_button: Radiobutton = Radiobutton(self, text=choice, variable=self.radio_button_variable, value=choice, bg='#383838', fg='white', selectcolor='black')
            radio_button.grid(row=1, column=i)
            self.radio_buttons.append(radio_button)

        self.submit_button: Button = Button(self, text="Submit", command=self.submit, width=20, height=2, font=('Times New Roman', 15), bg="#343434", fg="white")
        self.submit_button.grid(row=2, column=0, columnspan=len(choices))

    def submit(self: MultipleChoiceQuestionField) -> None:
        """ What to do when submit button is pressed.

        Args:
            self (MultipleChoiceQuestionField): Self.
        """
        self.submit_func(self.radio_button_variable.get())
