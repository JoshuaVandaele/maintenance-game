import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# FIXME: The interface should be separated from the logic of the game.
#        It should also be designed in a way that it can be easily extended.
#        For example, if you want to add a new question, you should only need to add a new entry to the questions list.
#        It should also be defined in a class, so that you can easily instantiate and manipulate it.
root = tk.Tk()
root.title("Quiz Game")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

question_label = tk.Label(root, text="texte question")
question_label.pack(fill=tk.X)
question_label.config(font=("Arial", 20))
question_label.pack()

entry = tk.Entry(root)
entry.insert(0, "Enter your answer here")
entry.config(width=50)
# FIXME: The position of the entry should be defined in a more flexible way.
entry.place(x=WINDOW_WIDTH / 2 - 150, y=WINDOW_HEIGHT / 2 - 20)

centered_radio_buttons_frame = tk.Frame(root)
centered_radio_buttons_frame.config(width=50)
centered_radio_buttons_frame.place(x=WINDOW_WIDTH / 2 - 100, y=WINDOW_HEIGHT / 2 - 20)

selected_option = tk.StringVar()

# FIXME: The radio buttons should be generated dynamically from the questions list.
radio_button = tk.Radiobutton(root, text="A", variable=selected_option, value="A")
radio_button.pack(in_=centered_radio_buttons_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="B", variable=selected_option, value="B")
radio_button.pack(in_=centered_radio_buttons_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="C", variable=selected_option, value="C")
radio_button.pack(in_=centered_radio_buttons_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="D", variable=selected_option, value="D")
radio_button.pack(in_=centered_radio_buttons_frame, side=tk.LEFT, padx=10)

submit_button = tk.Button(root, text="Submit", command=lambda: submit_handler())
# Stylize the submit button
submit_button.config(width=20, height=2, bg="#000000", fg="#ffffff")
submit_button.pack(side=tk.BOTTOM, pady=10)

result_label = tk.Label(root, text="")
result_label.config(font=("Arial", 20))
result_label.pack(fill=tk.X)
result_label.pack(side=tk.BOTTOM, pady=10)
result_label.pack()


def switch_mode():
    """This function is called when the quiz needs to change between QCM and entry mode."""
    # FIXME: Globals should be avoided. Instead, you should pass the variables as arguments to the function, or use a class.
    global mode
    if mode == "qcm":
        mode = "entry"
        entry.place(x=500, y=500)
        centered_radio_buttons_frame.place(
            x=WINDOW_WIDTH / 2 - 100, y=WINDOW_HEIGHT / 2 - 20
        )
    else:
        mode = "qcm"
        entry.place(x=WINDOW_WIDTH / 2 - 150, y=WINDOW_HEIGHT / 2 - 20)
        centered_radio_buttons_frame.place(x=500, y=500)


def check_answer(answer):
    # FIXME: Global variables should be avoided. Instead, you should pass the variables as arguments to the function, or use a class.
    global q
    if "q" not in globals():
        q = 0
    # FIXME: Questions and answers should be stored in a list or a dictionary, so that you can easily add new questions.
    if q == 0:
        return answer == "Paris"
    elif q == 1:
        return answer == "A"
    elif q == 2:
        return answer == "Rome"


# FIXME: This should be moved to a separate file, and the features of the function should be separated into multiple functions.
def submit_handler():
    """This function is called when the user clicks the submit button.
    It checks if the answer is correct or not and displays a message accordingly.
    If the answer is correct, it also moves on to the next question.
    """
    # FIXME: Global variables should be avoided. Instead, you should pass the variables as arguments to the function, or use a class.
    global selected_option
    global q
    global mode
    # FIXME: Avoid code duplication. You should not repeat the same code multiple times.
    if "q" not in globals():
        q = 0
    # FIXME: The logic of the game should be separated from the interface.
    answer = entry.get() if q != 1 else selected_option
    if check_answer(answer):
        result_label.config(text="Correct!")
        q += 1
    else:
        result_label.config(text="Wrong!")

    if q == 1:
        mode = "qcm"
        question_label.config(text="What is the capital of Germany?")
    elif q == 2:
        mode = "entry"
        question_label.config(text="What is the capital of Italy?")
    else:
        question_label.config(text="You have completed the quiz!")
        entry.pack_forget()
        centered_radio_buttons_frame.pack_forget()
        submit_button.pack_forget()
    switch_mode()


# hide radio buttons
question_label.config(text="What is the capital of France?")
mode = "entry"
switch_mode()

if __name__ == "__main__":
    root.mainloop()
