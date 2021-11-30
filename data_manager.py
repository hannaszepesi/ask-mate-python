import csv
import os
import database_common


dirname = os.path.dirname(__file__)
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
ANSWER_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/answer.csv'
QUESTION_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/question.csv'
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']
ORDER_OPTIONS = ['ascending', 'descending']

def get_max_id(path):
    input_file = list(csv.DictReader(open(path)))
    next_id = int(input_file[-1]['id'])+1
    return next_id


def get_data(path):
    data_list = []
    input_file = csv.DictReader(open(path))
    for questions in input_file:
        data_list.append(questions)
    return data_list


@database_common.connection_handler
def write_data(cursor):
    query = """
    INSERT INTO tablename (submission_time, view_number, vote_number, title, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, view_number, vote_number, title, message, image))


def modify_question_vote(id, vote, path, header):
    lines = get_data(path)
    for line in lines:
        if line['id'] == id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, path, header)


def modify_answer_vote(answer_id, vote, path, header):
    lines = get_data(path)
    for line in lines:
        if line['id'] == answer_id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, path, header)


def delete_an_answer(answer_id):
    answer_file = get_data(ANSWER_PATH)
    # with open(answer_file, 'r') as list_of_dict:
    for i in range(len(answer_file)-1):
        if answer_file[i]['id'] == answer_id:
            answer_file.pop(i)
        write_data(answer_file, ANSWER_PATH, ANSWER_HEADER)


@database_common.connection_handler
def delete_a_question(cursor, question_id):
    query = """
        DELETE from question
        WHERE question_id = %s;"""
    cursor.execute(query, (question_id,))


def get_question_by_id(id):
    questions = get_data(QUESTION_PATH)
    for question in questions:
        if question['id'] == id:
            return question #returns question as dictionary


@database_common.connection_handler
def modify_question(cursor,  new_title, new_message, image_path, question_id):
    query = """
            UPDATE question
            SET new_title, new_message, image_path = %s, %s, %s
            WHERE question_id = %s;"""
    cursor.execute(query, (new_title, new_message, image_path, question_id,))
