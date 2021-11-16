import csv
import os

QUESTION_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']
ANSWER_HEADER = ['id','submission_time','vote_number','question_id','message,image']

def get_questions():
    question_list = []
    with open('/home/hannaszepesi/Documents/Projects/WEB/WEEK 1/1st TW Week/ask-mate-1-python-HaruNoKitsune/sample_data/question.csv'):
        input_file = csv.DictReader(open('/home/hannaszepesi/Documents/Projects/WEB/WEEK 1/1st TW Week/ask-mate-1-python-HaruNoKitsune/sample_data/question.csv'))
    for questions in input_file:
        question_list.append(questions)
    return question_list

def get_answers():
    answer_list = []
    with open('sample_data/answer.csv'):
        input_file = csv.DictReader('sample_data/answer.csv')
    for answers in input_file:
        answer_list.append(answers)
    return answer_list

def write_answers(answers):
    with open('sample_data/answer.csv', 'w', newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames=ANSWER_HEADER)
        dictwriter_object.writeheader()
        for answer in answers:
            dictwriter_object.writerow(answer)

def write_quiestions(questions):
    with open('sample_data/answer.csv', 'w', newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames=QUESTION_HEADER)
        dictwriter_object.writeheader()
        for question in questions:
            dictwriter_object.writerow(question)