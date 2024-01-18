# <========== Imports ==========>

from __future__ import annotations
import unittest

# <========== Local Import ==========>

# Model
from Model.Question import Question
from Model.OpenQuestion import OpenQuestion
from Model.MultipleChoiceQuestion import MultipleChoiceQuestion

# Controller
from Controller.QuestionController import QuestionController

# <========== Tests ==========>

class TestCheckAnswer(unittest.TestCase):

    # <----- Open Question ----->

    def test_open_question_good_answer(self: TestCheckAnswer) -> None:
        question: OpenQuestion = OpenQuestion("What is the capital of France?", ["Paris"])
        self.assertTrue(question.check_answer("Paris"))

    def test_open_question_bad_answer(self: TestCheckAnswer) -> None:
        question: OpenQuestion = OpenQuestion("What is the capital of France?", ["Paris"])
        self.assertFalse(question.check_answer("Rome"))

    # <----- Multiple Choice Question ----->

    def test_multiple_choice_question_good_answer(self: TestCheckAnswer) -> None:
        question: MultipleChoiceQuestion = MultipleChoiceQuestion("What is the capital of Germany?", ["D"], ["A", "B", "C", "E", "F", "G", "H"])
        self.assertTrue(question.check_answer(["D"]))

    def test_multiple_choice_question_bad_answer(self: TestCheckAnswer):
        question: MultipleChoiceQuestion = MultipleChoiceQuestion("What is the capital of Germany?", ["D"], ["A", "B", "C", "E", "F", "G", "H"])
        self.assertFalse(question.check_answer(["A"]))
        self.assertFalse(question.check_answer(["A", "B"]))
        self.assertFalse(question.check_answer(["D", "A"]))
        self.assertFalse(question.check_answer(["A", "D"]))

class TestController(unittest.TestCase):

    def test_controller_check_good_answer(self: TestController) -> None:
        questions: list[Question] = [
            OpenQuestion("What is the capital of France?", ["Paris"]),
            OpenQuestion("What is the capital of Germany?", ["Berlin"]),
            MultipleChoiceQuestion("What is the capital of Italy?", ["Rome"], ["Paris", "Berlin", "Madrid", "Rome", "London", "Lisbon", "Brussels"])
        ]
        controller: QuestionController = QuestionController(questions)

        self.assertTrue(controller.check_answer("Paris"))
        self.assertTrue(controller.check_answer("Berlin"))
        self.assertTrue(controller.check_answer("Rome"))

    def test_controller_check_bad_answer(self: TestController) -> None:
        questions: list[Question] = [
            OpenQuestion("What is the capital of France?", ["Paris"]),
            OpenQuestion("What is the capital of Germany?", ["Berlin"]),
            MultipleChoiceQuestion("What is the capital of Italy?", ["Rome"], ["Paris", "Berlin", "Madrid", "Rome", "London", "Lisbon", "Brussels"])
        ]

        controller: QuestionController = QuestionController(questions)

        self.assertFalse(controller.check_answer("Rome"))
        self.assertFalse(controller.check_answer("Paris"))
        self.assertFalse(controller.check_answer("Berlin"))

    def test_next_question(self: TestController) -> None:
        questions: list[Question] = [
            OpenQuestion("What is the capital of France?", ["Paris"]),
            OpenQuestion("What is the capital of Germany?", ["Berlin"]),
            MultipleChoiceQuestion("What is the capital of Italy?", ["Rome"], ["Paris", "Berlin", "Madrid", "Rome", "London", "Lisbon", "Brussels"])
        ]

        controller: QuestionController = QuestionController(questions)

        self.assertTrue(controller.current_question_index == 0)
        self.assertTrue(controller.questions[0].text == "What is the capital of France?")
        self.assertTrue(controller.questions[controller.current_question_index].text == "What is the capital of France?")

        controller.next_question()

        self.assertTrue(controller.current_question_index == 1)
        self.assertTrue(controller.questions[1].text == "What is the capital of Germany?")
        self.assertTrue(controller.questions[controller.current_question_index].text == "What is the capital of Germany?")


    def test_it_is_end(self: TestController) -> None:
        questions: list[Question] = [
            OpenQuestion("What is the capital of France?", ["Paris"]),
            OpenQuestion("What is the capital of Germany?", ["Berlin"]),
            MultipleChoiceQuestion("What is the capital of Italy?", ["Rome"], ["Paris", "Berlin", "Madrid", "Rome", "London", "Lisbon", "Brussels"])
        ]

        controller: QuestionController = QuestionController(questions)

        self.assertFalse(controller.it_is_end())
        controller.next_question()
        self.assertFalse(controller.it_is_end())
        controller.next_question()
        self.assertFalse(controller.it_is_end())
        controller.next_question()
        self.assertTrue(controller.it_is_end())

        controller = QuestionController(questions)
        controller.check_answer("Paris")
        self.assertFalse(controller.it_is_end())
        controller.check_answer("Berlin")
        self.assertFalse(controller.it_is_end())
        controller.check_answer("Rome")
        self.assertTrue(controller.it_is_end())
# <========== Main ==========>

if __name__ == "__main__":
    unittest.main()
