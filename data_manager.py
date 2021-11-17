import csv
import os
dirname = os.path.dirname(__file__)
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
ANSWER_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/answer.csv'
QUESTION_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/question.csv'
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
        dictwriter_object.writerow(answers)


def write_questions(questions):
    with open(QUESTION_PATH, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=QUESTION_HEADER)
        writer.writeheader()
        for question in questions:
            writer.writerow(question)


