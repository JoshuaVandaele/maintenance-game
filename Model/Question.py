"""Question module."""

# <========== Imports ==========>

from __future__ import annotations

from abc import ABC, abstractmethod

# <========== Class ==========>


class Question(ABC):
    """Class representing a question.
    Abstract class (ABC).
    """

    @abstractmethod
    def __init__(self: Question, text: str, answer: list[str]) -> None:
        """Constructor for Question abstract class

        Args:
            text (str): Text of the question.
            answer (str | list[str]): Answer of the question, can be a list of answers.
        """
        self.text: str = text
        self.answer: list[str] = answer

    @abstractmethod
    def check_answer(self: Question, answer: str | list[str]) -> bool:
        """How to check if the answer is correct.

        Args:
            self (Question): Self.
            answer (str | list[str]): What answer to check.

        Returns:
            bool: if the answer is correct.
        """
        ...
