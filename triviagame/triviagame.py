#Tandem project to take in trivia questions from a JSON file, and allow users to take the quiz via CLI
from gamelogic import run_game

#Variables
trivia_questions = './Apprentice_TandemFor400_Data.json'

if __name__ == '__main__':
    run_game(trivia_questions)