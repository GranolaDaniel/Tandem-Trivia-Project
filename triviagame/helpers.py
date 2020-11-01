import json

from PyInquirer import prompt, Separator
from random import shuffle

#Parse the JSON file and return the conents as 'content'
def parse_json(jsonFile):
    with open(jsonFile) as f:
        content = json.load(f)
        return content

#Verify whether or not the user's answer was correct. Returns 1 if it is correct so that the user's score can be incremented (else returns 0)
def validate_answer(answer, correct_answer):
    if len(answer) != 0:
        if answer == correct_answer:
            print('That\'s correct!')
            return 1
        else:
            print('The correct answer is {}'.format(correct_answer))
            return 0
    else:
        print('Please enter an answer')

#Takes in a question, and formats it for use with PyInquirer. Returns the full, formatted question
def format_question(question, index):
    answers_list = question['incorrect']
    answers_list.append(question['correct'])
    #Randomizes the order of questions so the correct question isn't always the last one
    shuffle(answers_list)

    #The format that PyInquirer will receive the question in
    formatted_question = {
    'type': 'list',
    'qmark': '>',
    'message': question['question'],
    'name': 'answer' + str(index),
    'choices': [ 
        Separator('======='),
    ],
    'correct_choice': question['correct'],
    #This filter takes the user's input and then compares that with the correct answer
    'filter': lambda answer: validate_answer(answer, question['correct'])
    }
    #Adds each answer to the question
    for answer in answers_list:
        formatted_question['choices'].append(
            {
            'name': answer
        },
        )
        
    return formatted_question