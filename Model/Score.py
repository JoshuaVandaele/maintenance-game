# <========== Imports ==========>

from __future__ import annotations

# <========== Class ==========>

class Score:
    """ Class representing the score of the player.
    Using for the scoring system.
    """

    def __init__(self: Score, score: int = 0) -> None:
        """The constructor for Score class.

        Args:
            self (Score): Self.
            score (int): the starting score.
        """
        self.score: int = score

    def increment(self: Score, points: int, malus: int) -> None:
        """Add points to the score.
        If malus is negative, it will be set to 0.
        malus represents the points lost when the player has a wrong answer.

        Args:
            self (Score): Self.
            points (int): Points to add.
        """
        if malus < 0:
            malus = 0
        self.score += points - malus
        print(f"Score: {self.score}")