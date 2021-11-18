import csv
import os

dirname = os.path.dirname(__file__)
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
ANSWER_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/answer.csv'
QUESTION_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/question.csv'
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']


def get_max_id(path):
    input_file = csv.DictReader(open(path))
    max_id = 0
    for row in input_file:
        max_id += 1
    return max_id


def get_data(path):
    data_list = []
    input_file = csv.DictReader(open(path))
    for questions in input_file:
        data_list.append(questions)
    return data_list


def write_data(type, PATH, HEADER):
    with open(PATH, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        for answer in type:
            writer.writerow(answer)


def modify_vote(id, vote, path, header):
    lines = get_data(path)
    for line in lines:
        if line['id'] == id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, path, header)


def delete_an_answer(answer_id):
    answer_file = get_answers()
    with open(answer_file, 'w') as csv_file:
        for i in range(len(answer_file)):
            if answer_file[i]['id'] == answer_id:
                del answer_file[i]
            write_answers(answer_file[i])
