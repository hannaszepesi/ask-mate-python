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

def get_max_id(cursor):
    input_file = list(csv.DictReader(open(path)))
    next_id = int(input_file[-1]['id'])+1
    return next_id

@database_common.connection_handler
def get_data(cursor):
    query = """
        SELECT *
        FROM question
        """
    cursor.execute(query)
    return cursor.fetchall()


def write_data(type, PATH, HEADER):
    with open(PATH, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        for answer in type:
            writer.writerow(answer)


def modify_question_vote(id, vote, path, header):
    lines = get_data(path)
    for line in lines:
        if line['id'] == id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, path, header)

@database_common.connection_handler
def modify_answer_vote(cursor, answer_id, vote):
    query = """
        UPDATE answer
        SET vote_number = vote_number + %(vote)s
        WHERE answer_id = %(answer_id)s;
        """
    cursor.execute(query, {"vote": vote, "answer_id": answer_id})


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

@database_common.connection_handler
def get_question_by_id(cursor, id):
    query = """
        SELECT *
        FROM question
        WHERE id = %(id)s
        """
    cursor.execute(query, {"id": id})
    return cursor.fetchall()


@database_common.connection_handler
def modify_question(cursor,  new_title, new_message, image_path, question_id):
    query = """
            UPDATE question
            SET new_title, new_message, image_path = %s, %s, %s
            WHERE question_id = %s;"""
    cursor.execute(query, (new_title, new_message, image_path, question_id,))
