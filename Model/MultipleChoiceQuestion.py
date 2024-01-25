"""Multiple choice question module."""

# <========== Imports ==========>

from __future__ import annotations

from Model.Question import Question

# <========== Class ==========>


class MultipleChoiceQuestion(Question):
    """Class representing a multiple choice question.
    Derived from abstract class Question.
    """

    def __init__(
        self: MultipleChoiceQuestion, text: str, answer: list[str], trap: list[str]
    ) -> None:
        """Constructor for OpenQuestion class

        Args:
            self (MultipleChoiceQuestion): Self.
            text (str): Text of the question.
            answer (str): Answer of the question.
            trap (list[str]): List of trap answers.
        """
        super().__init__(text, answer)
        self.trap: list[str] = trap

    def check_answer(self: MultipleChoiceQuestion, answer: list[str]) -> bool:
        """Checks if the answer is correct.
        When answer is multiple choice, all choices must be correct.

        Args:
            answer (str | list[str]): Answer to check.

        Returns:
            bool: True if the answer is correct, if answer have multiple choices, all choices must be correct. False otherwise.
        """
        if isinstance(answer, str):
            return answer in self.answer
        return all(choice in self.answer for choice in answer)
