import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="texte question")
question_label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=lambda: check_answer())
submit_button.pack()


def check_answer():
    global q
    if "q" not in globals():
        q = 0
    user_answer = entry.get()
    if q == 0:
        if user_answer == "Paris":
            result_label.config(text="Correct!")
            question_label.config(text="What is the capital of Germany?")
            q += 1
        else:
            result_label.config(text="Wrong!")
    elif q == 1:
        if user_answer == "Berlin":
            result_label.config(text="Correct!")
            question_label.config(text="What is the capital of Italy?")
            q += 1
        else:
            result_label.config(text="Wrong!")
    elif q == 2:
        if user_answer == "Rome":
            result_label.config(text="Correct!")
            question_label.config(text="You won!")
            q += 1
        else:
            result_label.config(text="Wrong!")


result_label = tk.Label(root, text="")
result_label.pack()

question_label.config(text="What is the capital of France?")
root.mainloop()
