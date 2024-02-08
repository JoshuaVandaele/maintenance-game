# <========== Imports  ==========>

from __future__ import annotations

from tkinter import Frame, Label, PhotoImage

# <========== Class  ==========>


class EndPage(Frame):
    """
    Representation of the End Page
    """

    def __init__(self: EndPage) -> None:
        super().__init__()

        self.image = PhotoImage(file="img/logo.png")
        self.image_label = Label(self, image=self.image)
        self.image_label.pack()
        self.text = Label(
            self, text="Bravo! Vous avez terminé cette partie", font=("Helvetica", 50)
        )
        self.text.pack(anchor="center")
