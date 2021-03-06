import unittest
import random
import string
import sys
sys.path.append('..')
from triviagame.helpers import parse_json, format_question, validate_answer

trivia_questions = '../triviagame/Apprentice_TandemFor400_Data.json'



def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class TestValidateAnswer(unittest.TestCase):
    def test_validate_correct(self):
        """
        Ensure that validate_answer() returns 1 if the answer matches the correct answer
        """
        answer1 = get_random_string(10)
        correct_answer = answer1

        test_answer = validate_answer(answer1, correct_answer)

        self.assertEqual(test_answer, 1)
    def test_validate_incorrect(self):
        """
        Ensure that validate_answer() returns 0 if the answer doesn't match the correct answer
        """
        answer1 = get_random_string(10)
        correct_answer = get_random_string(9)

        test_answer = validate_answer(answer1, correct_answer)

        self.assertEqual(test_answer, 0)


if __name__ == '__main__':
    unittest.main()