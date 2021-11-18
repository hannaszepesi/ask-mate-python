import csv
import os
dirname = os.path.dirname(__file__)
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
ANSWER_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/answer.csv'
QUESTION_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/question.csv'
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']
ORDER_OPTIONS = ['ascending', 'descending']

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


def modify_vote(id, vote):
    lines = get_data(QUESTION_PATH)
    for line in lines:
        if line['id'] == id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, QUESTION_PATH, QUESTION_HEADER)




def delete_an_answer(answer_id):
    answer_file = get_data(ANSWER_PATH)
    # with open(answer_file, 'r') as list_of_dict:
    for dict in range(len(answer_file)-1):
        if answer_file[dict]['id'] == answer_id:
            del answer_file[dict]
        write_data(answer_file, ANSWER_PATH, ANSWER_HEADER)



