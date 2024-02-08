import unittest

from Controller.QuestionController import QuestionController


class TestGenerateQuestion(unittest.TestCase):
    def test_generate_questions(self):
        questions = QuestionController.generate_questions(10)
        self.assertEqual(len(questions), 10)


if __name__ == "__main__":
    unittest.main()
