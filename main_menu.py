import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

class Page(tk.Frame):
    """
    Representation of a single page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        self.tkraise()

class WelcomePage(Page):
    """
    Representation of the Welcome Page
    """
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        label_quizz = tk.Label(self, text="Welcome in Quiz Game!")
        label_quizz.config(font=("Arial", 20))
        label_quizz.pack()

        start_button = tk.Button(self, text="Start the game", height=2, width=30, command=lambda: controller.show_frame(GamePage))
        start_button.pack(pady=8)

        quit_button = tk.Button(self, text="Leave the game", height=2, width=30, command=controller.quit)
        quit_button.pack(pady=8)

class GamePage(Page):
    """
    Representation of the page showing questions
    """
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        label_quizz = tk.Label(self, text="Game is in progress...")
        label_quizz.config(font=("Arial", 20))
        label_quizz.pack()

        back_button = tk.Button(self, text="Back to Welcome", height=2, width=30, command=lambda: controller.show_frame(WelcomePage))
        back_button.pack(pady=8)

class Application(tk.Tk):
    """
    Representation of the tkinter app for handling pages
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Quiz Game")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, GamePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        """
        Method for showing a single page
        """
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
