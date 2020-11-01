from PyInquirer import prompt
from random import shuffle

from helpers import parse_json, format_question

#Runs the main game loop. Takes in questions to ask, and the number of questions to ask the user (default is 10)
def run_game(game_questions, num_questions=10):

    game_questions = parse_json(game_questions)
    shuffle(game_questions)

    preformatted_list = []
    formatted_list = []

    while len(preformatted_list) != 10:
        preformatted_list.append(game_questions.pop())

    for idx in range(0, num_questions):
        formatted_list.append(format_question(preformatted_list[idx], idx+1))
    
    answers = prompt(formatted_list)
    final_score = sum(answers.values())
    
    print('Your final score is {}/{}'.format(final_score, num_questions))