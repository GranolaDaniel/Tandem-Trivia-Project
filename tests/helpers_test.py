import unittest

import sys
sys.path.append('..')
from triviagame.helpers import parseJSON, formatQuestion

triviaQuestions = '../triviagame/Apprentice_TandemFor400_Data.json'

def test_dupe(testList):
    for item in testList:
        if testList.count(item) > 1:
            return True
    return False

class TestHelperFunctions(unittest.TestCase):
    def test_no_repeats(self):
        """
        Ensure that users are given unique questions
        """
        game_questions = parse_json(trivia_questions)
        questions_list = []

        while len(questions_list) != 10:
            questions_list.append(format_question(game_questions.pop()))
        
        self.assertFalse(test_dupe(questions_list))



if __name__ == '__main__':
    unittest.main()