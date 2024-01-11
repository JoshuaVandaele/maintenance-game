import unittest

from main import check_answer


class TestCheckAnswer(unittest.TestCase):
    def test_question_0(self):
        global q
        q = 0
        self.assertTrue(check_answer("Paris"))

    def test_wrong_answer(self):
        global q
        q = 0
        self.assertFalse(check_answer("Wrong Answer"))


if __name__ == "__main__":
    unittest.main()
