import tkinter as tk
import json

# FIXME: The interface should be separated from the logic of the game.
#        It should also be designed in a way that it can be easily extended.
#        For example, if you want to add a new question, you should only need to add a new entry to the questions list.
#        It should also be defined in a class, so that you can easily instantiate and manipulate it.
root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="texte question")
question_label.pack()

entry = tk.Entry(root)
entry.pack()

center_frame = tk.Frame(root)
center_frame.pack()

selected_option = tk.StringVar()

# FIXME: The radio buttons should be generated dynamically from the questions list.
radio_button = tk.Radiobutton(root, text="A", variable=selected_option, value="0")
radio_button.pack(anchor=tk.W)
radio_button.pack(in_=center_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="B", variable=selected_option, value="1")
radio_button.pack(anchor=tk.W)
radio_button.pack(in_=center_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="C", variable=selected_option, value="2")
radio_button.pack(anchor=tk.W)
radio_button.pack(in_=center_frame, side=tk.LEFT, padx=10)

radio_button = tk.Radiobutton(root, text="D", variable=selected_option, value="3")
radio_button.pack(anchor=tk.W)
radio_button.pack(in_=center_frame, side=tk.LEFT, padx=10)

submit_button = tk.Button(root, text="Submit", command=lambda: submit_handler())
submit_button.pack()

def load_questions():
    """This function loads the questions from the questions.json file and returns them as a list.
    """
    questions = json.load(open("questions.json"))
    return questions

def check_answer(answer):
    """This function checks if the answer is correct or not.
    It returns True if the answer is correct, and False otherwise.
    Use the global variable q to keep track of the current question.
    """
    # FIXME: Global variables should be avoided. Instead, you should pass the variables as arguments to the function, or use a class.
    global q

    if "q" not in globals():
        q = 0
    # FIXME: Questions and answers should be stored in a list or a dictionary, so that you can easily add new questions.
    if q == 0:
        return answer == load_questions()[0]["answer"]

    # FIXME: Use answer in json file instead of hardcoding it.
    elif q == 1:
        return answer == "1"


# FIXME: This should be moved to a separate file, and the features of the function should be separated into multiple functions.
def submit_handler():
    """This function is called when the user clicks the submit button.
    It checks if the answer is correct or not and displays a message accordingly.
    If the answer is correct, it also moves on to the next question.
    """
    # FIXME: Global variables should be avoided. Instead, you should pass the variables as arguments to the function, or use a class.
    global selected_option
    global q
    # FIXME: Avoid code duplication. You should not repeat the same code multiple times.
    if "q" not in globals():
        q = 0
    # FIXME: The logic of the game should be separated from the interface.
    answer = entry.get() if q != 1 else selected_option.get()
    if check_answer(answer):
        result_label.config(text="Correct!")
        q += 1
    else:
        result_label.config(text="Wrong!")

    if q == 1:
        question_label.config(text=load_questions()[1]["answer"])
        center_frame.pack()
        entry.pack_forget()
    else:
        question_label.config(text="You have completed the quiz!")
        entry.pack_forget()
        center_frame.pack_forget()
        submit_button.pack_forget()


result_label = tk.Label(root, text="")
result_label.pack()

# hide radio buttons
center_frame.pack_forget()
question_label.config(text=load_questions()[0]["question"])
root.mainloop()
