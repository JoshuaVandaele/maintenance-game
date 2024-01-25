# <========== Imports ==========>

from __future__ import annotations

# <========== Local Imports ==========>

from Model.Question import Question

# <========== Class ==========>

class OpenQuestion(Question):
    """ Class representing a open question.
    Derived from abstract class Question.
    """

    def __init__(self: OpenQuestion, text: str, answer: list[str]) -> None:
        """ Constructor for OpenQuestion class

        Args:
            self (OpenQuestion): Self.
            text (str): Text of the question.
            answer (str): Answer of the question.
        """
        super().__init__(text, answer)

    def check_answer(self: OpenQuestion, answer: str) -> bool:
        """ Checks if the answer is correct.

        Args:
            answer (str | list[str]): Answer to check.

        Returns:
            bool: True if the answer is correct, all choices must be correct. False otherwise.
        """
        return answer in self.answer