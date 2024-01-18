# <========== Imports ==========>

from __future__ import annotations
from tkinter import Frame, Tk

# <========== Local Imports ==========>

# Model Imports
from Model.Question import Question
from Model.OpenQuestion import OpenQuestion
from Model.MultipleChoiceQuestion import MultipleChoiceQuestion

# View Imports
from View.OpenQuestionField import OpenQuestionField
from View.MultipleChoiceQuestionField import MultipleChoiceQuestionField

# <========== Class ==========>

class QuestionController:
    """ Controller using to manage the questions.
    Create a view for each question and check the answer.
    """

    def __init__(self: QuestionController, questions: list[Question]) -> None:
        """ The constructor for QuestionController class.

        Args:
            self (QuestionController): Self.
            questions (list[Question]): All Questions to display.
        """
        self.questions: list[Question] = questions
        self.current_question_index: int = 0

        self.root: Tk = Tk()
        self.root.title("Quiz Game")

        self.current_view: Frame | None  = None
        self.load_view()

    def check_answer(self: QuestionController, answer: str | list[str]) -> None:
        """ Check if the answer is correct.
        if the answer is correct, go to the next question.

        Args:
            self (QuestionController): Self.
            answer (str | list[str]): Answer to check.
        """
        if self.questions[self.current_question_index].check_answer(answer):
            self.next_question()

    def next_question(self: QuestionController) -> None:
        """ Go to the next question.
        load the view of the next question.

        Args:
            self (QuestionController): Self.
        """
        self.current_question_index += 1
        if not self.it_is_end():
            self.load_view()

    def load_view(self: QuestionController) -> None:
        """ Load the view of the current question.
        The view change depending of the type of the question.
        The view is a tkinter Frame.s

        Args:
            self (QuestionController): Self.
        """
        if self.current_view:
            self.current_view.pack_forget()

        if isinstance(self.questions[self.current_question_index], OpenQuestion):
            self.current_view = OpenQuestionField(
                label_text=self.questions[self.current_question_index].text,
                submit_func=self.check_answer
            )
        elif isinstance(self.questions[self.current_question_index], MultipleChoiceQuestion):
            self.current_view = MultipleChoiceQuestionField(
                label_text=self.questions[self.current_question_index].text,
                choices=self.questions[self.current_question_index].answer + self.questions[self.current_question_index].trap,  # type: ignore
                submit_func=self.check_answer
            )
        else:
            self.current_view = Frame()

        self.current_view.pack(in_=self.root)

    def it_is_end(self: QuestionController) -> bool:
        """ Check if it is the end of the game.
        if the index of the current question is equal to the length of the questions list, it is the end of the game.

        Args:
            self (QuestionController): Self.

        Returns:
            bool: True if it is the end of the game, False otherwise.
        """
        return self.current_question_index == len(self.questions)