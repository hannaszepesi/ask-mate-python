import csv
import os

QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message,image']
ANSWER_PATH = "sample_data/answer.csv"
QUESTION_PATH = "sample_data/question.csv"
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']

def get_max_id():
    input_file = csv.DictReader(open(QUESTION_PATH))
    max_id = 0
    for row in input_file:
        max_id += 1
    return max_id


def get_questions():
    question_list = []
    input_file = csv.DictReader(open(QUESTION_PATH))
    for questions in input_file:
        question_list.append(questions)
    return question_list


def get_answers():
    answer_list = []
    input_file = csv.DictReader(open(ANSWER_PATH))
    for answers in input_file:
        answer_list.append(answers)
    return answer_list


def write_answers(answers):
    with open(ANSWER_PATH, 'a', newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames=ANSWER_HEADER)
        dictwriter_object.writeheader()
        for answer in answers:
            dictwriter_object.writerow(answer)


def write_questions(questions):
    with open(QUESTION_PATH, 'a', newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames=QUESTION_HEADER)
        dictwriter_object.writeheader()
        dictwriter_object.writerow(questions)
